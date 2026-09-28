# ZDL downloads

This directory contains the ready-to-install effects distributed by this repository.

**Target devices:** MS-50G · MS-70G · MS-60B · G1on · G1Xon · B1on.

For the effect catalog, direct download links, Zoom Effect Manager installation instructions and release ZIPs, see the [main README](../README.md).

## Keep packaged effects together

If an effect has its own directory, keep the complete directory together: the `.ZDL`, matching `.json`, image/icon and any other accompanying files belong to one effect package.

Release builds publish each top-level effect directory as its own ZIP so it can be extracted directly into the custom-effects folder used by Zoom Effect Manager.

## Notes

- Test custom effects carefully and keep a backup of your existing effects/presets.
- Not every effect has been hardware-tested on every target device.
- Hardware behavior can depend on pedal model, firmware, the rest of the chain and total DSP load.
- IR-loader variants can become too heavy at long FIR lengths or in larger effect chains.
- The DSP cost value in experimental/custom ZDLs is not a reliable CPU percentage.

For building your own cabinet banks, see [HYBRID IR](https://github.com/Leemuzhko/HYBRID-IR).
