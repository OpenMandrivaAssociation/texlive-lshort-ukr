%global tl_name lshort-ukr
%global tl_revision 55643

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.00
Release:	%{tl_revision}.1
Summary:	Ukrainian version of the LaTeX introduction
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/ukrainian
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-ukr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-ukr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Ukrainian version of A Short Introduction to LaTeX2e.

