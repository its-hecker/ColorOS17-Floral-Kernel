# ColorOS 17 / floral kernel adapter (Pixel 4 XL)

Maintainer: **Hecker**. Stage-0 integration repo, **not** a fork or a bootable kernel yet.

Our known Android 17 floral kernel is pinned in `source.json`. The boot chain will use the existing hardware-validated Linux 4.14 source. This repository owns ColorOS-specific kernel/boot compatibility tests and future patches; upstream kernel content is fetched **separately** by the local-manifest workspace. Never flash output from this initial stage.

Run `python3 tools/audit_kernel.py /path/to/heckeros-floral-kernel` after checking out the pinned upstream commit.

The kernel source has a KernelSU submodule. Keep its pinned gitlink; do not enable new root functionality as part of the first-boot port.
