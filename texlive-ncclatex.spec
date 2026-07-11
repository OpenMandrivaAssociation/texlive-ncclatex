%global tl_name ncclatex
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	An extended general-purpose class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ncclatex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ncclatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ncclatex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The ncc class provides a framework for a common class to replace the
standard article, book and report classes, and providing a "preprint"
class. The class's extensions are provided in a number of small
packages, some of which may also be used with the standard classes. The
ncclatex package also loads many of the packages of, and requires the
latest version of the ncctools bundle.

