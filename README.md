# goodix-fp-local-config

System config for the Goodix **27c6:5110** fingerprint reader on Fedora, packaged
so `dnf` manages it (survives reinstall/reboot). Companion to the
`libfprint-goodixtls` COPR (the actual driver).

Ships:
- `/usr/lib/udev/rules.d/60-goodix-fp-no-autosuspend.rules` — disables USB
  autosuspend for the sensor. **Required**: autosuspend makes the device
  re-enumerate mid-verify ("No such device"), breaking the goodixtls driver.
- `/usr/share/polkit-1/rules.d/60-greeter-fprintd.rules` — lets the greetd
  greeter user (`greeter`) use fprintd. **Optional**: only needed if you enable
  fingerprint at the login screen; harmless otherwise.

**Not shipped:** the TLS PSK. It is secret and per-machine; recover it into
`/etc/goodix-fp/psk.bin` (root 600) separately.

## Install
```
sudo dnf copr enable hkoeck/goodix-fp-local-config
sudo dnf install goodix-fp-local-config
```
If you previously placed the rules by hand in `/etc/`, remove those copies so the
packaged (vendor) ones own them:
```
sudo rm -f /etc/udev/rules.d/60-goodix-fp-no-autosuspend.rules \
           /etc/polkit-1/rules.d/60-greeter-fprintd.rules
```

## Build locally
```
make -f .copr/Makefile srpm outdir=/tmp/out && rpmbuild --rebuild /tmp/out/*.src.rpm
```
