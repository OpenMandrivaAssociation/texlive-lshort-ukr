# revision 15878
# category Package
# catalog-ctan /info/lshort/ukrainian
# catalog-date 2008-08-22 10:50:40 +0200
# catalog-license other-free
# catalog-version 4.00
Name:		texlive-lshort-ukr
Version:	4.00
Release:	2
Summary:	Ukrainian version of the LaTeX introduction
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/ukrainian
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-ukr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-ukr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Ukrainian version of A Short Introduction to LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-ukr/lshort-ukr-4.12.src.tar.gz
%doc %{_texmfdistdir}/doc/latex/lshort-ukr/lshort-ukr.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.00-2
+ Revision: 753521
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.00-1
+ Revision: 718907
- texlive-lshort-ukr
- texlive-lshort-ukr
- texlive-lshort-ukr
- texlive-lshort-ukr

