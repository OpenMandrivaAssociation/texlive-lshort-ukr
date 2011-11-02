Name:		texlive-lshort-ukr
Version:	4.00
Release:	1
Summary:	Ukrainian version of the LaTeX introduction
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/ukrainian
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-ukr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-ukr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
