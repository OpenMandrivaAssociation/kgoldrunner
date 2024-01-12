Summary:	A game of action and puzzle solving
Name:		plasma6-kgoldrunner
Version:	24.01.90
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://games.kde.org/game.php?game=kgoldrunner
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kgoldrunner-%{version}.tar.xz
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(Phonon4Qt6)

%description
KGoldrunner is an action game where the hero runs through a maze, climbs
stairs, dig holes and dodges enemies in order to collect all the gold nuggets
and escape to the next level. Your enemies are also after the gold. Worse
still, they are after you!.

%files -f kgoldrunner.lang
%{_datadir}/qlogging-categories6/kgoldrunner.categories
%{_bindir}/kgoldrunner
%{_datadir}/kgoldrunner
%{_iconsdir}/hicolor/*/apps/kgoldrunner.png
%{_datadir}/knsrcfiles/kgoldrunner.knsrc
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.xml

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kgoldrunner-%{?git:master}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja
%ninja

%install
%ninja_install -C build
%find_lang kgoldrunner --all-name --with-html
