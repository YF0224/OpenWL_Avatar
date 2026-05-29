"""
gen_ue_avatar/funcs — decoupled functional modules for the UE avatar pipeline.

Each file provides one focused capability:
  - gen_tpose.py        : generate T-pose RGBA image from reference
  - gen_3d_avatar.py    : generate 3D avatar mesh from T-pose image (via Trellis)
  - gen_scene.py        : generate 3D scene (via FlashWorld / HunyuanWorldPlay)
  - gen_motion.py       : skeleton detection + motion generation
  - import_ue.py        : import 3D assets into Unreal Engine 5 via Python bridge
"""
