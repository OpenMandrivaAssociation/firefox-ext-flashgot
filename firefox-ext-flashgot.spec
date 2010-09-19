%define realname flashgot
%define debug_package %{nil}

%define _mozillaextpath %{firefox_mozillapath}/extensions

Summary: Flashgot extension for firefox
Name: firefox-ext-%{realname}
Version: 1.2.1.31
Release: %mkrel 1
License: GPLv2+
Group: Networking/WWW
URL: http://flashgot.net
Source: https://addons.mozilla.org/en-US/firefox/downloads/file/45660/flashgot-%version-fx+mz+sm+tb.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: firefox = %{firefox_epoch}:%{firefox_version}
Obsoletes: mozilla-firefox-ext-%{realname} < %{version}-%{release}
Provides: mozilla-firefox-ext-%{realname} = %{version}-%{release}
Suggests: kget curl gwget
BuildRequires: firefox-devel

%description
FlashGot is the free Mozilla / Firefox / Flock / Thunderbird extension
(compatible with Netscape too), meant to handle single and massive ("all"
and "selection") downloads with several external Download Managers.

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %firefox_mozillapath
%{_mozillaextpath}
