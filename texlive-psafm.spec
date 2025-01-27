# revision 13293
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-psafm
Version:	20111104
Release:	12
Summary:	TeXLive psafm package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psafm.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive psafm package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/itc/psafm/stonesan/is8b8a.afm
%{_texmfdistdir}/fonts/afm/itc/psafm/stonesan/is8bi8a.afm
%{_texmfdistdir}/fonts/afm/itc/psafm/stonesan/is8r8a.afm
%{_texmfdistdir}/fonts/afm/itc/psafm/stonesan/is8ri8a.afm
%{_texmfdistdir}/fonts/afm/itc/psafm/stonesan/is8s8a.afm
%{_texmfdistdir}/fonts/afm/itc/psafm/stonesan/is8si8a.afm

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 755142
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719315
- texlive-psafm
- texlive-psafm
- texlive-psafm
- texlive-psafm

