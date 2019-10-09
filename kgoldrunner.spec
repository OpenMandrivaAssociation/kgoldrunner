Summary:	A game of action and puzzle solving
Name:		kgoldrunner
Version:	19.08.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://games.kde.org/game.php?game=kgoldrunner
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(Phonon4Qt5)

%description
KGoldrunner is an action game where the hero runs through a maze, climbs
stairs, dig holes and dodges enemies in order to collect all the gold nuggets
and escape to the next level. Your enemies are also after the gold. Worse
still, they are after you!.

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/kgoldrunner.categories
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_sysconfdir}/xdg/%{name}.knsrc
%{_datadir}/applications/*.desktop
%{_datadir}/kxmlgui5/%{name}
%{_datadir}/metainfo/*.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5 -G Ninja
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
