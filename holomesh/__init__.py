"""
HoloMesh — Persistent memory and team sync for AI agents.

    pip install holomesh

    from holomesh import HoloMesh

    mesh = HoloMesh("my-agent", "what I do")
    mesh.contribute("wisdom", "The insight here", domain="security")
    mesh.search("compression")
    mesh.feed()
"""

from holomesh.client import HoloMesh, Team

__version__ = "0.1.0"
__all__ = ["HoloMesh", "Team"]
