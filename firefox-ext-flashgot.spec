Summary: Flashgot extension for firefox
Name: firefox-ext-flashgot
Version: 1.2.8.4
Release: %mkrel 1
License: GPLv2+
Group: Networking/WWW
URL: http://flashgot.net
Source: http://releases.mozilla.org/pub/mozilla.org/addons/220/flashgot-%version-fx+tb+sm.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: firefox >= %{firefox_epoch}:%{firefox_version}
Obsoletes: mozilla-firefox-ext-flashgot < %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
Suggests: kget curl gwget
BuildRequires: firefox-devel

%description
FlashGot is the free Mozilla / Firefox / Flock / Thunderbird extension
(compatible with Netscape too), meant to handle single and massive ("all"
and "selection") downloads with several external Download Managers.

%prep
%setup -q -c -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}
