from argparse import Namespace
from timm.data.constants import IMAGENET_DEFAULT_MEAN
from timm.data.constants import IMAGENET_DEFAULT_STD
import torchvision.transforms.functional as F

from configs.__base__ import *


class cfg(cfg_common, cfg_dataset_default, cfg_model_cdo):
	def __init__(self):
		cfg_common.__init__(self)
		cfg_dataset_default.__init__(self)
		cfg_model_cdo.__init__(self)

		self.vis = True
		self.fvcore_b = 1
		self.fvcore_c = 3
		self.seed = 42

		self.epoch_full = 100
		self.warmup_epochs = 0
		self.test_start_epoch = self.epoch_full
		self.test_per_epoch = self.epoch_full // 2

		self.batch_train = 12
		self.batch_test_per = 12
		self.lr = 0.0005 * self.batch_train / 16
		self.weight_decay = 0.05

		self.use_adeval = True

		###### Train DATA
		self.train_data.cls_names = ['Ring']
		self.test_data.cls_names = ['Ring']

		self.train_data.anomaly_generator.name = 'white_noise'
		self.train_data.anomaly_generator.enable = True ### TODO
		self.train_data.anomaly_generator.kwargs = dict()

		# ==> model
		checkpoint_path = 'model/pretrain/wide_resnet50_racm-8234f177.pth'
		self.model_t = Namespace()
		self.model_t.name = 'mshrnet32' ### TODO
		self.model_t.kwargs = dict(pretrained=True, checkpoint_path='',strict=False)

		self.model_s = Namespace()
		self.model_s.name = 'mshrnet32'
		self.model_s.kwargs = dict(pretrained=False, checkpoint_path='', strict=False)

		# self.model_t = Namespace()
		# self.model_t.name = 'timm_wide_resnet50_2'
		# self.model_t.kwargs = dict(pretrained=True, checkpoint_path=None,
		# 						   strict=False, features_only=True, out_indices=[1, 2, 3])
		#
		# self.model_s = Namespace()
		# self.model_s.name = 'timm_wide_resnet50_2'
		# self.model_s.kwargs = dict(pretrained=False, checkpoint_path=None,
		# 						   strict=False, features_only=True, out_indices=[1, 2, 3])

		self.model = Namespace()
		self.model.name = 'cdo'
		self.model.kwargs = dict(pretrained=False, checkpoint_path='', strict=False,
								 model_t=self.model_t, model_s=self.model_s)

		# ==> optimizer
		self.optim.lr = self.lr
		self.optim.kwargs = dict(name='adam', betas=(0.5, 0.999))

		# ==> trainer
		self.trainer.name = 'CDOTrainer'
		self.trainer.logdir_sub = 'exp1'
		self.trainer.resume_dir = ''
		self.trainer.epoch_full = self.epoch_full
		self.trainer.scheduler_kwargs = dict(
			name='step', lr_noise=None, noise_pct=0.67, noise_std=1.0, noise_seed=42, lr_min=self.lr / 1e2,
			warmup_lr=self.lr / 1e3, warmup_iters=-1, cooldown_iters=0, warmup_epochs=self.warmup_epochs, cooldown_epochs=0, use_iters=True,
			patience_iters=0, patience_epochs=0, decay_iters=0, decay_epochs=int(self.epoch_full * 0.8), cycle_decay=0.1, decay_rate=0.1)

		self.trainer.test_start_epoch = self.test_start_epoch
		self.trainer.test_per_epoch = self.test_per_epoch

		self.trainer.data.batch_size = self.batch_train
		self.trainer.data.batch_size_per_gpu_test = self.batch_test_per

		# ==> loss
		self.loss.loss_terms = [
			dict(type='CDOLoss', name='cdo_loss', gamma=2, OOM=True),
		] ### TODO

		# ==> logging
		self.logging.log_terms_train = [
			dict(name='batch_t', fmt=':>5.3f', add_name='avg'),
			dict(name='data_t', fmt=':>5.3f'),
			dict(name='optim_t', fmt=':>5.3f'),
			dict(name='lr', fmt=':>7.6f'),
			dict(name='cdo_loss', suffixes=[''], fmt=':>5.3f', add_name='avg'),
		]
		self.logging.log_terms_test = [
			dict(name='batch_t', fmt=':>5.3f', add_name='avg'),
			dict(name='cdo_loss', suffixes=[''], fmt=':>5.3f', add_name='avg'),
		]
