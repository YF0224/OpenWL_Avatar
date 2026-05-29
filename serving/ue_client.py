"""
ue_client.py — UE5 RPC client for pushing generated assets to Unreal Engine.

Communicates with UE5 via the Python Remote Control Plugin (HTTP RPC).

Functions:
    import_avatar_to_ue  — push a 3D avatar asset into the UE5 project
    import_scene_to_ue   — push a 3D scene asset into the UE5 project
    import_motion_to_ue  — push and bind a motion file to an avatar in UE5
"""


UE_RPC_HOST = "http://localhost:30010"  # UE5 Remote Control Plugin default port


def import_avatar_to_ue(avatar_path: str) -> bool:
    """
    Push a 3D avatar asset into the current UE5 project via RPC.

    Args:
        avatar_path: Path to the .glb / .fbx avatar file.

    Returns:
        True if import succeeded.
    """
    raise NotImplementedError


def import_scene_to_ue(scene_path: str) -> bool:
    """
    Push a 3D scene asset into the current UE5 project via RPC.

    Args:
        scene_path: Path to the .glb / .usd scene file.

    Returns:
        True if import succeeded.
    """
    raise NotImplementedError


def import_motion_to_ue(motion_path: str, avatar_name: str) -> bool:
    """
    Push and bind a motion file to an avatar in UE5 via RPC.

    Args:
        motion_path:  Path to the .bvh / .fbx motion file.
        avatar_name:  Name of the avatar asset in UE5 to bind the motion to.

    Returns:
        True if import succeeded.
    """
    raise NotImplementedError
