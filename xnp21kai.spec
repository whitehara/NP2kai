Name:           xnp21kai
Version:        22
Release:        20240101%{?dist}
Summary:        Neko Project 2 Kai - PC-9801 series emulator with IA-32

License:        MIT
URL:            https://github.com/AZO234/NP2kai
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ cmake
BuildRequires:	git openssl-devel libusb1-devel SDL2-devel SDL2_mixer-devel SDL2_ttf-devel gtk2-devel libX11-devel fontconfig-devel freetype-devel
Requires:       SDL2 SDL2_mixer gtk2 SDL2_ttf openssl-libs libusb1 gtk2 fontconfig freetype libX11

%description
Neko Project 2 Kai is PC-9801 series emulator
This version is compiled for IA-32 version
See https://github.com/AZO234/NP2kai


%prep
%autosetup

%build
mkdir build
cd build
cmake .. -D BUILD_X=ON -D USE_SDL2=ON -D CMAKE_INSTALL_PREFIX=/usr
%make_build


%install
cd build
%make_install

mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/ja/man1

mv %{buildroot}%{_mandir}/xnp21kai.1 %{buildroot}%{_mandir}/man1/xnp21kai.1
gzip -9 %{buildroot}%{_mandir}/man1/xnp21kai.1
mv %{buildroot}%{_mandir}/xnp21kai.1j %{buildroot}%{_mandir}/ja/man1/xnp21kai.1
gzip -9 %{buildroot}%{_mandir}/ja/man1/xnp21kai.1


%files
%license LICENSE
%doc README.md
%{_bindir}/xnp21kai
%{_mandir}/man1/xnp21kai.1.gz
%{_mandir}/ja/man1/xnp21kai.1.gz
%{_datadir}/applications/xnp21kai.desktop
%{_datadir}/icons/hicolor/scalable/apps/np2.svg



%changelog
* Mon Jan 01 2024 Shiro Hara <white@vx-xv.com>
- Update source 20240101

* Thu Jun 15 2023 Shiro Hara <white@vx-xv.com>
- Update source 20230615

* Sun Jan 22 2023 Shiro Hara <white@vx-xv.com>
- Update source "Jul 31 2022"

* Mon Mar 14 2022 Shiro Hara <white@vx-xv.com>
- Add .spec file for creating rpm. You can create .rpm file by rpmbuild.
