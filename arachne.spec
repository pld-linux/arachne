Summary:	Arachne - web browser
Summary(es.UTF-8):   Navegador de Internet Arachne
Summary(pl.UTF-8):   Arachne - przeglądarka WWW
Summary(pt_BR.UTF-8):   Navegador Arachne
Name:		arachne
Version:	1.66b
Release:	2
License:	distributable (see LICENSE)
Group:		Applications/Networking
Source0:	http://browser.arachne.cz/%{name}-%{version}.tar.gz
# Source0-md5:	2e51c4951114814f60daf5484975c59b
URL:		http://browser.arachne.cz/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveOS:	Linux
ExclusiveArch:	%{ix86}

%description
Small and fast web browser.

%description -l pl.UTF-8
Szybka, mała, nieźle się prezentująca przeglądarka WWW.

%package common
Summary:	Configuration files for Arachne
Summary(pl.UTF-8):   Pliki konfiguracyjne używane przez Arachne
Group:		Applications/Networking
Requires:	glibc >= 2.1

%description common
Files shared between svgalib and ggi versions of Arachne.

%description common -l pl.UTF-8
Pliki konfiguracyjne używane przez obie wersje Arachne.

%package svga
Summary:	Arachne web browser for svgalib
Summary(pl.UTF-8):   Wersja przeglądarki Arachne korzystająca z svgalib
Group:		Applications/Networking
Requires:	arachne-common

%description svga
Arachne is web browser. This is beta release for svgalib. Arachne uses
external programs to convert JPEGs (djpeg) and PNGs(convert) to BMPs,
because BMP are faster to display. Few interesting ideas are
introduced by Arachne.

Information on the license may be found in the file
%{_docdir}/%{name}-common-%{version}/LICENSE.

%description svga -l pl.UTF-8
To jest wersja beta przeglądarki WWW - Arachne, która korzysta z
biblioteki svgalib. Arachne jest szybka i mała, niestety nie obsługuje
jeszcze protokołu HTTPS ani JavaScriptu, ani CSS.

Informacje na temat licencji można znaleźć w pliku
%{_docdir}/%{name}-common-%{version}/LICENSE.

%package ggi
Summary:	Arachne web browser for ggi
Summary(pl.UTF-8):   Wersja przeglądarki Arachne korzystająca z biblioteki ggi
Group:		X11/Applications/Networking
Requires:	arachne-common

%description ggi
Arachne is web browser. This is beta release for ggi. Arachne uses
external programs to convert JPEGs (djpeg) and PNGs(convert) to BMPs,
because BMP are faster to display. Few interesting ideas are
introduced by Arachne.

Information on the license may be found in the file
%{_docdir}/%{name}-common-%{version}/LICENSE.

%description ggi -l pl.UTF-8
To jest wersja beta przeglądarki WWW - Arachne, która korzysta z
biblioteki ggi. Arachne jest szybka i mała, niestety nie obsługuje
jeszcze protokołu HTTPS ani JavaScriptu, ani CSS.

Informacje na temat licencji można znaleźć w pliku
%{_docdir}/%{name}-common-%{version}/LICENSE.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/arachne,%{_prefix}/doc}

install bin/* $RPM_BUILD_ROOT%{_bindir}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
cp -rf share/arachne/* $RPM_BUILD_ROOT%{_datadir}/arachne

ln -sf %{_docdir}/arachne-common-%{version} $RPM_BUILD_ROOT%{_prefix}/doc/arachne

cat > $RPM_BUILD_ROOT%{_bindir}/arachne << EOF
#!/bin/sh
if [ "\$TERM" = "linux" ]; then
	exec %{_bindir}/arachne-svgalib $@
else
	exec %{_bindir}/arachne-ggi $@
fi
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc doc/arachne/{CHANGES,KEYWORDS,LICENSE,README,*.txt}
%attr(755,root,root) %{_bindir}/arachne
%{_mandir}/man1/*
%dir %{_prefix}/doc
%{_prefix}/doc/arachne
%dir %{_datadir}/arachne
%{_datadir}/arachne/[g-t]*
%attr(755,root,root) %{_datadir}/arachne/arachne-install

%files ggi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arachne-ggi

%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arachne-svgalib
