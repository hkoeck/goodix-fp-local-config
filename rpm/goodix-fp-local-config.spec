Name:           goodix-fp-local-config
Version:        1
Release:        1%{?dist}
Summary:        Local udev + polkit config for the Goodix 27c6:5110 fingerprint reader

License:        MIT
URL:            https://github.com/hkoeck/goodix-fp-local-config
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
System configuration to make the Goodix 27c6:5110 fingerprint reader usable on
this machine:
 * a udev rule that disables USB autosuspend for the sensor (autosuspend makes
   it re-enumerate mid-verify and breaks the goodixtls driver), and
 * a polkit rule letting the greetd greeter user verify via fprintd (only
   relevant if fingerprint-at-login is enabled; harmless otherwise).

The TLS PSK itself is secret and per-machine and is NOT shipped here; see the
goodix-fp notes for how it is recovered into /etc/goodix-fp/psk.bin.

%prep
%autosetup -n %{name}-%{version}

%install
install -Dm644 rules/60-goodix-fp-no-autosuspend.rules \
  %{buildroot}%{_prefix}/lib/udev/rules.d/60-goodix-fp-no-autosuspend.rules
install -Dm644 rules/60-greeter-fprintd.rules \
  %{buildroot}%{_datadir}/polkit-1/rules.d/60-greeter-fprintd.rules

%files
%{_prefix}/lib/udev/rules.d/60-goodix-fp-no-autosuspend.rules
%{_datadir}/polkit-1/rules.d/60-greeter-fprintd.rules

%changelog
* Sat Oct 17 2026 hkoeck - 1-1
- Initial: ship the no-autosuspend udev rule and the greeter fprintd polkit rule.
