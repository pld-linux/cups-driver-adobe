# TODO
# - check license. adding nosource as licensing is not clear
Summary:	Adobe Universal PostScript Windows Driver
Summary(pl):	Uniwersalny sterownik postscriptowy Adobe dla Windows
Name:		cups-driver-adobe
Version:	1.0.6
Release:	0.1
License:	?
Group:		Applications/Printing
Source0:	http://download.adobe.com/pub/adobe/printerdrivers/win/1.x/winsteng.exe
# NoSource0-md5:	1038eac5b9fcd8985ced069fbdb13cb8
NoSource:	0
URL:		http://www.adobe.com/support/downloads/product.jsp?product=44&platform=Windows
BuildRequires:	cabextract
BuildRequires:	cups-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_datadir	%(cups-config --datadir 2>/dev/null)
%define 	_cupsdriverdir	%{_datadir}/drivers

%description
This package contains Adobe Universal PostScript Windows Driver of
supported Microsoft Windows platform:
- AdobePS 4.5.3: Windows 95, Windows 98, Windows 98 Second Edition, or
  Windows Millennium Edition
- AdobePS 5.2.2: Windows NT 4.0
- PScript 5: Windows 2000 or Windows XP

These drivers enable you to print documents from applications running
in these Windows platforms to any printer that includes Adobe
PostScript Level 2 or Adobe PostScript 3.

This printer driver was jointly developed by Adobe Systems
Incorporated and Microsoft Corporation.

This is the Windows driver support package for use with Samba.

%description -l pl
Ten pakiet zawiera uniwersalny sterownik postscriptowy Adobe dla
Windows (Adobe Universal PostScript Windows Driver) dla obs³ugiwanych
platform Microsoft Windows:
- AdobePS 4.5.3 dla Windows 95, Windows 98, Windows 98 Second Edition
  i Windows Millennium Edition
- AdobePS 5.2.2 dla Windows NT 4.0
- PScript 5 dla Windows 2000 i Windows XP

Sterowniki te pozwalaj± na drukowanie dokumentów z aplikacji
dzia³aj±cych pod wy¿ej wymienionymi platformami Windows na dowolnej
drukarce obs³uguj±cej Adobe PostScript Level 2 lub Adobe PostScript 3.

Ten sterownik drukarki powsta³ we wspó³pracy miêdzy Adobe Systems
Incorporated i Microsoft Corporation.

Jest to pakiet wspieraj±cy sterownik windowsowy do u¿ywania z Samb±.

%prep
%setup -qcT
cabextract -L %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_cupsdriverdir}
# perhaps need all platforms
cp -a winxp/* $RPM_BUILD_ROOT%{_cupsdriverdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_cupsdriverdir}/*
