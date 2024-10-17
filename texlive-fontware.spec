Name:		texlive-fontware
Version:	70015
Release:	1
Summary:	TeXLive fontware package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontware.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontware.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-fontware.bin

%description
TeXLive fontware package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/pltotf.1*
%doc %{_texmfdistdir}/doc/man/man1/pltotf.man1.pdf
%doc %{_mandir}/man1/tftopl.1*
%doc %{_texmfdistdir}/doc/man/man1/tftopl.man1.pdf
%doc %{_mandir}/man1/vftovp.1*
%doc %{_texmfdistdir}/doc/man/man1/vftovp.man1.pdf
%doc %{_mandir}/man1/vptovf.1*
%doc %{_texmfdistdir}/doc/man/man1/vptovf.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
