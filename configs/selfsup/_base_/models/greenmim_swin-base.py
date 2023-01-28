# model settings
img_size = 224
patch_size = 4

model = dict(
    type='GreenMIM',
    data_preprocessor=dict(
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        bgr_to_rgb=True),
    backbone=dict(
        type='GreenMIMSwinTransformer',
        arch='B',
        img_size=img_size,
        patch_size=patch_size,
        drop_path_rate=0.0,
        stage_cfgs=dict(block_cfgs=dict(window_size=7))),
    neck=dict(type='GreenMIMNeck', in_channels=3, encoder_stride=32, img_size=img_size, patch_size=patch_size),
    head=dict(
        type='GreenMIMHead',
        patch_size=patch_size,
        norm_pix_loss=False,
        loss=dict(type='SimMIMReconstructionLoss', encoder_in_channels=3)))
