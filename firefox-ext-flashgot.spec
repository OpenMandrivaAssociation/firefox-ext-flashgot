Summary: Flashgot extension for firefox
Name: firefox-ext-flashgot
Version: 1.2.9.4
Release: 3
License: GPLv2+
Group: Networking/WWW
URL: https://flashgot.net
Source: https://secure.informaction.com/download/releases/flashgot-%{version}.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: firefox >= %{firefox_version}
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


%changelog
* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 1.2.9.4-1mdv2011.0
+ Revision: 673420
- new version 1.2.9.4
- new version 1.2.9.3

* Sat Mar 19 2011 Funda Wang <fwang@mandriva.org> 1.2.8.4-1
+ Revision: 646524
- new version 1.2.8.4

* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 1.2.8.1-1
+ Revision: 633593
- New version 1.2.8.1

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 1.2.6-2mdv2011.0
+ Revision: 628872
- rebuild for new firefox

* Sat Dec 11 2010 Funda Wang <fwang@mandriva.org> 1.2.6-1mdv2011.0
+ Revision: 620582
- renew tarball
- update to new version 1.2.6

* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1.2.5-1mdv2011.0
+ Revision: 598963
- update to new version 1.2.5

* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 1.2.1.31-2mdv2011.0
+ Revision: 597400
- rebuild for new firefox

* Sun Sep 19 2010 Funda Wang <fwang@mandriva.org> 1.2.1.31-1mdv2011.0
+ Revision: 579781
- new version 1.2.1.3

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - rebuild for firefox-3.6.8

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 1.2.1.26-3mdv2011.0
+ Revision: 561168
- rebuild for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 1.2.1.26-2mdv2010.1
+ Revision: 549360
- Rebuild with FF 3.6.6

  + Funda Wang <fwang@mandriva.org>
    - New version 1.2.1.26

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 1.2.1.18-1mdv2010.1
+ Revision: 531262
- update to new version 1.2.1.18

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 1.2.1.17-2mdv2010.1
+ Revision: 531093
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 1.2.1.17-1mdv2010.1
+ Revision: 527008
- update to new version 1.2.1.17

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 1.2.1.09-1mdv2010.1
+ Revision: 494853
- update to new version 1.2.1.09

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 1.2.1.04-2mdv2010.1
+ Revision: 494798
- rebuild

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 1.2.1.04-1mdv2010.1
+ Revision: 480371
- new version 1.2.1.04 (ff 3.6b5)

* Tue Nov 10 2009 Funda Wang <fwang@mandriva.org> 1.2.0.8-1mdv2010.1
+ Revision: 463978
- new version 1.2.0.8

* Wed Sep 16 2009 Funda Wang <fwang@mandriva.org> 1.2.0.4-1mdv2010.0
+ Revision: 443382
- New version 1.2.0.4

* Tue Aug 18 2009 Gustavo De Nardin <gustavodn@mandriva.com> 1.2-2mdv2010.0
+ Revision: 417670
- buildrequire firefox-devel, which provides the new macros for building extensions
- make use of the firefox package macros
- rebuild for firefox 3.5.2

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 1.2-1mdv2010.0
+ Revision: 410557
- new version 1.2

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 1.1.9-4mdv2010.0
+ Revision: 410506
- rebuild for new ff

* Fri Jul 31 2009 Funda Wang <fwang@mandriva.org> 1.1.9-3mdv2010.0
+ Revision: 405030
- rebuild for new ff

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 1.1.9-2mdv2010.0
+ Revision: 385774
- rebuild for new ff

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 1.1.9-1mdv2010.0
+ Revision: 381240
- New version 1.1.9

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1.1.8.6-1mdv2010.0
+ Revision: 369810
- New version 1.1.8.6

* Sat Mar 28 2009 Gustavo De Nardin <gustavodn@mandriva.com> 1.1.7.9-2mdv2009.1
+ Revision: 361850
- rebuild for firefox 3.0.8

* Thu Mar 12 2009 Funda Wang <fwang@mandriva.org> 1.1.7.9-1mdv2009.1
+ Revision: 354098
- New version 1.1.7.9

* Wed Feb 04 2009 Funda Wang <fwang@mandriva.org> 1.1.7.7-1mdv2009.1
+ Revision: 337315
- rename to firefox
- New version 1.1.7.7
- rename to firefox

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 1.1.4-2mdv2009.1
+ Revision: 318921
- rebuild for new ff

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 1.1.4-1mdv2009.1
+ Revision: 303705
- new version 1.1.4

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 1.0.5-2mdv2009.0
+ Revision: 289175
- rebuild for new FF

* Tue Aug 12 2008 Funda Wang <fwang@mandriva.org> 1.0.5-1mdv2009.0
+ Revision: 271156
- New version 1.0.5

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 1.0.4.5-1mdv2009.0
+ Revision: 257897
- New version 1.0.4.5

  + Tiago Salem <salem@mandriva.com.br>
    - add conditional to ff3

* Wed Jul 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.4.2-3mdv2009.0
+ Revision: 236362
- rebuilt for mozilla-firefox-2.0.0.16

* Thu Jul 03 2008 Tiago Salem <salem@mandriva.com.br> 1.0.4.2-2mdv2009.0
+ Revision: 231259
- Rebuild for firefox 2.0.0.15

* Sun Jun 29 2008 Funda Wang <fwang@mandriva.org> 1.0.4.2-1mdv2009.0
+ Revision: 229993
- New version 1.0.4.2

* Tue May 27 2008 Funda Wang <fwang@mandriva.org> 1.0-1mdv2009.0
+ Revision: 211542
- New version 1.0

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.9.9-1mdv2009.0
+ Revision: 201021
- New version 0.9.9

* Sat Apr 19 2008 Funda Wang <fwang@mandriva.org> 0.9.7-1mdv2009.0
+ Revision: 195739
- New version 0.9.7

* Tue Apr 15 2008 Funda Wang <fwang@mandriva.org> 0.9.5-1mdv2009.0
+ Revision: 193986
- New version 0.9.5

* Wed Mar 26 2008 Tiago Salem <salem@mandriva.com.br> 0.8.1-2mdv2008.1
+ Revision: 190329
- bump ff_ver and release

* Sat Mar 01 2008 Funda Wang <fwang@mandriva.org> 0.8.1-1mdv2008.1
+ Revision: 177074
- New version 0.8.1

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 0.7.9-1mdv2008.1
+ Revision: 164618
- New version 0.7.9

* Sat Jan 05 2008 Funda Wang <fwang@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 145661
- New version 0.7.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Thierry Vignaud <tv@mandriva.org> 0.7-2mdv2008.1
+ Revision: 117793
- own firefox directories so that they're not left behind on uninstall

* Wed Dec 12 2007 Funda Wang <fwang@mandriva.org> 0.7-1mdv2008.1
+ Revision: 117656
- New version 0.7

* Wed Dec 12 2007 Funda Wang <fwang@mandriva.org> 0.6.9.9-2mdv2008.1
+ Revision: 117623
- rebuild for new ff

* Sun Nov 18 2007 Funda Wang <fwang@mandriva.org> 0.6.9.9-1mdv2008.1
+ Revision: 109780
- Suggests gwget and kget
- suggests aria2 curl
- import source and spec
- Created package structure for mozilla-firefox-ext-flashgot.

