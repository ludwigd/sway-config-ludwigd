%global srcname sway-config-ludwigd

Name:           sway-config-ludwigd
Version:        1.0.0
Release:        1%{?dist}
Summary:        ludwigd's configuration for Sway
License:        GPLv3+
BuildArch:      noarch
Requires:       sway >= 1.7
Provides:       sway-config = %{version}-%{release}
Conflicts:      sway-config

URL: https://github.com/ludwigd/%{srcname}
# Sources can be obtained by
# git clone https://github.com/ludwigd/sway-config-ludwigd
# cd sway-config-ludwigd
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

Requires:       brightnessctl
Requires:       clipman
Requires:       desktop-backgrounds-compat
Requires:       foot
Requires:       grim
Requires:       i3status
Requires:       rofi-wayland
Requires:       swaybg
Requires:       swaycaffeine
Requires:       swayidle
Requires:       swaylock
Requires:       wireplumber
Requires:       yaws

%description
ludwigd's Sway config

%prep
%autosetup

%build
# nothing to build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/sway
install -m 644 ./config %{buildroot}/%{_sysconfdir}/sway/config

%files
%config(noreplace) %{_sysconfdir}/sway/config

%changelog
* Thu Jan 23 2025 Damian Ludwig <ludwigd@fedoraproject.org> 1.0.0-1
- new package built with tito

