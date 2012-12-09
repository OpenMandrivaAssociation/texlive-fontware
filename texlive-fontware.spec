# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-fontware
Version:	20111103
Release:	2
Summary:	TeXLive fontware package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontware.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontware.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-fontware.bin

%description
TeXLive fontware package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/pltotf.1*
%doc %{_texmfdir}/doc/man/man1/pltotf.man1.pdf
%doc %{_mandir}/man1/tftopl.1*
%doc %{_texmfdir}/doc/man/man1/tftopl.man1.pdf
%doc %{_mandir}/man1/vftovp.1*
%doc %{_texmfdir}/doc/man/man1/vftovp.man1.pdf
%doc %{_mandir}/man1/vptovf.1*
%doc %{_texmfdir}/doc/man/man1/vptovf.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 752047
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718487
- texlive-fontware
- texlive-fontware
- texlive-fontware
- texlive-fontware

