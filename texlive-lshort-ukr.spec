Name:		texlive-lshort-ukr
Version:	55643
Release:	1
Summary:	Ukrainian version of the LaTeX introduction
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/ukrainian
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-ukr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-ukr.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
