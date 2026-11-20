# ColorOS 17 kernel/boot assessment

- Use the existing coral/floral 4.14 kernel; ColorOS GSI binaries **do not** provide a matching Pixel boot image.
- Preserve Pixel-specific DTB, firmware, CHRE/Soli, Citadel and FaceAuth support.
- Validate the vendor/kernel interface and boot ramdisk against actual extracted donor metadata before altering init or fstab.
- Audit kernel eBPF/backports required by the Android 17 userspace before any first-boot package.
- Do not reuse the OnePlus 7 Pro boot, dtbo, vbmeta or kernel. Its identical chipset family does not imply partition or panel compatibility.
- Initial goal is a boot-chain **audit**, not a prebuilt image; secure boot/verity policies must be reviewed explicitly rather than globally disabled without a test rationale.
