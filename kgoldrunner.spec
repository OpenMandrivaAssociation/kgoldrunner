Summary:	A game of action and puzzle solving
Name:		kgoldrunner
Version:	15.12.3
Release:	2
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://games.kde.org/game.php?game=kgoldrunner
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	cmake(KDEGames)

%description
KGoldrunner is an action game where the hero runs through a maze, climbs
stairs, dig holes and dodges enemies in order to collect all the gold nuggets
and escape to the next level. Your enemies are also after the gold. Worse
still, they are after you!.

%files
%{_bindir}/%{name}
%{_datadir}/applications/kde4/KGoldrunner.desktop
%{_datadir}/apps/kgoldrunner
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/config/kgoldrunner.knsrc
%doc %{_docdir}/*/*/%{name}

#------------------------------------------------------------------------------

%prep
%setup -q
sed -i '1s/^/cmake_minimum_required(VERSION 3.1)\n/' CMakeLists.txt

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
