%define		kdeappsver	21.12.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kmines
Summary:	kmines
Name:		ka5-%{kaname}
Version:	21.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	239cb66699d48bdb078fd2024f533d40
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMines is a classic Minesweeper game. The idea is to uncover all the
squares without blowing up any mines. When a mine is blown up, the
game is over.

%description -l pl.UTF-8
KMines jest klasyczną grą w Sapera. Celem gry jest odkrycie wszystkich
kwadratów bez trafiania na miny. Gdy mina wybuchnie, gra jest skończona.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmines
%{_desktopdir}/org.kde.kmines.desktop
%{_iconsdir}/hicolor/128x128/apps/kmines.png
%{_iconsdir}/hicolor/16x16/apps/kmines.png
%{_iconsdir}/hicolor/22x22/apps/kmines.png
%{_iconsdir}/hicolor/32x32/apps/kmines.png
%{_iconsdir}/hicolor/48x48/apps/kmines.png
%{_iconsdir}/hicolor/64x64/apps/kmines.png
%{_datadir}/kmines
%{_datadir}/metainfo/org.kde.kmines.appdata.xml
%{_datadir}/qlogging-categories5/kmines.categories
