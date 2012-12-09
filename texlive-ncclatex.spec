# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ncclatex
# catalog-date 2007-02-23 22:01:12 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-ncclatex
Version:	1.5
Release:	2
Summary:	An extended general-purpose class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ncclatex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ncclatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ncclatex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The ncc class provides a framework for a common class to
replace the standard article, book and report classes, and
providing a "preprint" class. The class's extensions are
provided in a number of small packages, some of which may also
be used with the standard classes. The ncclatex package also
loads many of the packages of, and requires the latest version
of the ncctools bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ncclatex/cp1251-light.def
%{_texmfdistdir}/tex/latex/ncclatex/ncc.cls
%{_texmfdistdir}/tex/latex/ncclatex/ncc10.clo
%{_texmfdistdir}/tex/latex/ncclatex/ncc11.clo
%{_texmfdistdir}/tex/latex/ncclatex/ncc12.clo
%{_texmfdistdir}/tex/latex/ncclatex/ncc14.clo
%{_texmfdistdir}/tex/latex/ncclatex/nccart.clo
%{_texmfdistdir}/tex/latex/ncclatex/nccbiblist.sty
%{_texmfdistdir}/tex/latex/ncclatex/nccbook.clo
%{_texmfdistdir}/tex/latex/ncclatex/nccdefaults.sty
%{_texmfdistdir}/tex/latex/ncclatex/nccfit.clo
%{_texmfdistdir}/tex/latex/ncclatex/ncchdr.sty
%{_texmfdistdir}/tex/latex/ncclatex/nccheadings.sty
%{_texmfdistdir}/tex/latex/ncclatex/nccindex.sty
%{_texmfdistdir}/tex/latex/ncclatex/ncclatex.sty
%{_texmfdistdir}/tex/latex/ncclatex/nccltrus.sty
%{_texmfdistdir}/tex/latex/ncclatex/nccold.sty
%{_texmfdistdir}/tex/latex/ncclatex/nccproc.cls
%{_texmfdistdir}/tex/latex/ncclatex/nccsections.sty
%{_texmfdistdir}/tex/latex/ncclatex/ncctheorems.sty
%{_texmfdistdir}/tex/latex/ncclatex/ncctitle.clo
%{_texmfdistdir}/tex/latex/ncclatex/ncctitle.sty
%{_texmfdistdir}/tex/latex/ncclatex/ncctitlepage.sty
%{_texmfdistdir}/tex/latex/ncclatex/sibjnm.cls
%doc %{_texmfdistdir}/doc/latex/ncclatex/README
%doc %{_texmfdistdir}/doc/latex/ncclatex/changes.txt
%doc %{_texmfdistdir}/doc/latex/ncclatex/manifest.txt
%doc %{_texmfdistdir}/doc/latex/ncclatex/ncclatex.pdf
%doc %{_texmfdistdir}/doc/latex/ncclatex/ncclatex.tex
%doc %{_texmfdistdir}/doc/latex/ncclatex/nccnews.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2
+ Revision: 754251
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 719104
- texlive-ncclatex
- texlive-ncclatex
- texlive-ncclatex
- texlive-ncclatex

