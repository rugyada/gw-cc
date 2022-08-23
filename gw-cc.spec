#REVISIONARE
Name:		gw-cc
Version:	0.3.0
Release:	1
Summary:	GWelcome Center
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/rugyada/gw-cc
Source0:	%{name}-%version.tar.gz
Requires:	kdialog
Requires:	dnf-plugins-core
Requires:	htmlscript >= 1.0.1
BuildRequires:	make
BuildArch:	noarch
%rename om-control-center

%description
OpenMandriva GWelcome Center

%prep
%setup -q
%autopatch -p1

%build
# Nothing to do here...

%install
%make_install

%find_lang gw-cc

mkdir -p %{buildroot}%{_datadir}/icons/
cp gw-cc.svg %{buildroot}%{_datadir}/icons/

%files -f gw-cc.lang
%{_bindir}/gw-cc
%{_datadir}/%{name}/*
%{_datadir}/applications/gw-cc.desktop
%{_datadir}/icons/gw-cc.svg
