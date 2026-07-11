%global tl_name fontware
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Tools for virtual font metrics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/knuth/dist/etc
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontware.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontware.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(fontware.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Virtual font metrics are usually created in a textual form, the Virtual
Property List, but programs that use them need to use binary files (the
Virtual Font and the TeX Font Metric). The present two programs
translate between the two forms: - vptovf takes a VPL file and generates
a VF file and a TFM file; - vftovp takes a VF file and a TFM file and
generates a VPL file. The programs are to be found in every distribution
of TeX.

