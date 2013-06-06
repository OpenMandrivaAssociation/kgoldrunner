Name:		kgoldrunner
Version:	4.10.4
Release:	1
Epoch:		1
Summary:	A game of action and puzzle solving
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kgoldrunner
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
KGoldrunner is an action game where the hero runs through a maze, climbs
stairs, dig holes and dodges enemies in order to collect all the gold nuggets
and escape to the next level. Your enemies are also after the gold. Worse
still, they are after you!.

%files
%{_kde_bindir}/kgoldrunner
%{_kde_applicationsdir}/KGoldrunner.desktop
%{_kde_configdir}/kgoldrunner.knsrc
%{_kde_appsdir}/kgoldrunner
%{_kde_docdir}/*/*/kgoldrunner
%{_kde_iconsdir}/hicolor/*/apps/kgoldrunner.png

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

