#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x090B11993D9AEBB5 (ludo@gnu.org)
#
Name     : guile
Version  : 2.2.6
Release  : 40
URL      : https://mirrors.kernel.org/gnu/guile/guile-2.2.6.tar.xz
Source0  : https://mirrors.kernel.org/gnu/guile/guile-2.2.6.tar.xz
Source99 : https://mirrors.kernel.org/gnu/guile/guile-2.2.6.tar.xz.sig
Summary  : GNU's Ubiquitous Intelligent Language for Extension (uninstalled)
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: guile-bin = %{version}-%{release}
Requires: guile-data = %{version}-%{release}
Requires: guile-lib = %{version}-%{release}
Requires: guile-license = %{version}-%{release}
Requires: guile-man = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : emacs
BuildRequires : glibc-locale
BuildRequires : gmp-dev
BuildRequires : libunistring-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(bdw-gc)
BuildRequires : pkgconfig(libffi)
BuildRequires : readline-dev
BuildRequires : sed
BuildRequires : texinfo

%description
This is version 2.2 of Guile, Project GNU's extension language library.
Guile is an implementation of the Scheme programming language, packaged
as a library that can be linked into applications to give them their own
extension language.  Guile supports other languages as well, giving
users of Guile-based applications a choice of languages.

%package bin
Summary: bin components for the guile package.
Group: Binaries
Requires: guile-data = %{version}-%{release}
Requires: guile-license = %{version}-%{release}

%description bin
bin components for the guile package.


%package data
Summary: data components for the guile package.
Group: Data

%description data
data components for the guile package.


%package dev
Summary: dev components for the guile package.
Group: Development
Requires: guile-lib = %{version}-%{release}
Requires: guile-bin = %{version}-%{release}
Requires: guile-data = %{version}-%{release}
Provides: guile-devel = %{version}-%{release}
Requires: guile = %{version}-%{release}

%description dev
dev components for the guile package.


%package doc
Summary: doc components for the guile package.
Group: Documentation
Requires: guile-man = %{version}-%{release}

%description doc
doc components for the guile package.


%package lib
Summary: lib components for the guile package.
Group: Libraries
Requires: guile-data = %{version}-%{release}
Requires: guile-license = %{version}-%{release}

%description lib
lib components for the guile package.


%package license
Summary: license components for the guile package.
Group: Default

%description license
license components for the guile package.


%package man
Summary: man components for the guile package.
Group: Default

%description man
man components for the guile package.


%prep
%setup -q -n guile-2.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1562011187
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1562011187
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/guile
cp COPYING %{buildroot}/usr/share/package-licenses/guile/COPYING
cp COPYING.LESSER %{buildroot}/usr/share/package-licenses/guile/COPYING.LESSER
cp LICENSE %{buildroot}/usr/share/package-licenses/guile/LICENSE
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/guile/2.2/ccache/ice-9/and-let-star.go
/usr/lib64/guile/2.2/ccache/ice-9/arrays.go
/usr/lib64/guile/2.2/ccache/ice-9/atomic.go
/usr/lib64/guile/2.2/ccache/ice-9/binary-ports.go
/usr/lib64/guile/2.2/ccache/ice-9/boot-9.go
/usr/lib64/guile/2.2/ccache/ice-9/buffered-input.go
/usr/lib64/guile/2.2/ccache/ice-9/calling.go
/usr/lib64/guile/2.2/ccache/ice-9/channel.go
/usr/lib64/guile/2.2/ccache/ice-9/command-line.go
/usr/lib64/guile/2.2/ccache/ice-9/common-list.go
/usr/lib64/guile/2.2/ccache/ice-9/control.go
/usr/lib64/guile/2.2/ccache/ice-9/curried-definitions.go
/usr/lib64/guile/2.2/ccache/ice-9/debug.go
/usr/lib64/guile/2.2/ccache/ice-9/deprecated.go
/usr/lib64/guile/2.2/ccache/ice-9/documentation.go
/usr/lib64/guile/2.2/ccache/ice-9/eval-string.go
/usr/lib64/guile/2.2/ccache/ice-9/eval.go
/usr/lib64/guile/2.2/ccache/ice-9/expect.go
/usr/lib64/guile/2.2/ccache/ice-9/fdes-finalizers.go
/usr/lib64/guile/2.2/ccache/ice-9/format.go
/usr/lib64/guile/2.2/ccache/ice-9/ftw.go
/usr/lib64/guile/2.2/ccache/ice-9/futures.go
/usr/lib64/guile/2.2/ccache/ice-9/gap-buffer.go
/usr/lib64/guile/2.2/ccache/ice-9/getopt-long.go
/usr/lib64/guile/2.2/ccache/ice-9/hash-table.go
/usr/lib64/guile/2.2/ccache/ice-9/hcons.go
/usr/lib64/guile/2.2/ccache/ice-9/history.go
/usr/lib64/guile/2.2/ccache/ice-9/i18n.go
/usr/lib64/guile/2.2/ccache/ice-9/iconv.go
/usr/lib64/guile/2.2/ccache/ice-9/lineio.go
/usr/lib64/guile/2.2/ccache/ice-9/list.go
/usr/lib64/guile/2.2/ccache/ice-9/local-eval.go
/usr/lib64/guile/2.2/ccache/ice-9/ls.go
/usr/lib64/guile/2.2/ccache/ice-9/mapping.go
/usr/lib64/guile/2.2/ccache/ice-9/match.go
/usr/lib64/guile/2.2/ccache/ice-9/networking.go
/usr/lib64/guile/2.2/ccache/ice-9/null.go
/usr/lib64/guile/2.2/ccache/ice-9/occam-channel.go
/usr/lib64/guile/2.2/ccache/ice-9/optargs.go
/usr/lib64/guile/2.2/ccache/ice-9/peg.go
/usr/lib64/guile/2.2/ccache/ice-9/peg/cache.go
/usr/lib64/guile/2.2/ccache/ice-9/peg/codegen.go
/usr/lib64/guile/2.2/ccache/ice-9/peg/simplify-tree.go
/usr/lib64/guile/2.2/ccache/ice-9/peg/string-peg.go
/usr/lib64/guile/2.2/ccache/ice-9/peg/using-parsers.go
/usr/lib64/guile/2.2/ccache/ice-9/poe.go
/usr/lib64/guile/2.2/ccache/ice-9/poll.go
/usr/lib64/guile/2.2/ccache/ice-9/popen.go
/usr/lib64/guile/2.2/ccache/ice-9/ports.go
/usr/lib64/guile/2.2/ccache/ice-9/posix.go
/usr/lib64/guile/2.2/ccache/ice-9/pretty-print.go
/usr/lib64/guile/2.2/ccache/ice-9/psyntax-pp.go
/usr/lib64/guile/2.2/ccache/ice-9/q.go
/usr/lib64/guile/2.2/ccache/ice-9/r5rs.go
/usr/lib64/guile/2.2/ccache/ice-9/rdelim.go
/usr/lib64/guile/2.2/ccache/ice-9/readline.go
/usr/lib64/guile/2.2/ccache/ice-9/receive.go
/usr/lib64/guile/2.2/ccache/ice-9/regex.go
/usr/lib64/guile/2.2/ccache/ice-9/runq.go
/usr/lib64/guile/2.2/ccache/ice-9/rw.go
/usr/lib64/guile/2.2/ccache/ice-9/safe-r5rs.go
/usr/lib64/guile/2.2/ccache/ice-9/safe.go
/usr/lib64/guile/2.2/ccache/ice-9/sandbox.go
/usr/lib64/guile/2.2/ccache/ice-9/save-stack.go
/usr/lib64/guile/2.2/ccache/ice-9/scm-style-repl.go
/usr/lib64/guile/2.2/ccache/ice-9/serialize.go
/usr/lib64/guile/2.2/ccache/ice-9/session.go
/usr/lib64/guile/2.2/ccache/ice-9/slib.go
/usr/lib64/guile/2.2/ccache/ice-9/stack-catch.go
/usr/lib64/guile/2.2/ccache/ice-9/streams.go
/usr/lib64/guile/2.2/ccache/ice-9/string-fun.go
/usr/lib64/guile/2.2/ccache/ice-9/suspendable-ports.go
/usr/lib64/guile/2.2/ccache/ice-9/syncase.go
/usr/lib64/guile/2.2/ccache/ice-9/textual-ports.go
/usr/lib64/guile/2.2/ccache/ice-9/threads.go
/usr/lib64/guile/2.2/ccache/ice-9/time.go
/usr/lib64/guile/2.2/ccache/ice-9/top-repl.go
/usr/lib64/guile/2.2/ccache/ice-9/unicode.go
/usr/lib64/guile/2.2/ccache/ice-9/vlist.go
/usr/lib64/guile/2.2/ccache/ice-9/weak-vector.go
/usr/lib64/guile/2.2/ccache/language/brainfuck/compile-scheme.go
/usr/lib64/guile/2.2/ccache/language/brainfuck/compile-tree-il.go
/usr/lib64/guile/2.2/ccache/language/brainfuck/parse.go
/usr/lib64/guile/2.2/ccache/language/brainfuck/spec.go
/usr/lib64/guile/2.2/ccache/language/bytecode.go
/usr/lib64/guile/2.2/ccache/language/bytecode/spec.go
/usr/lib64/guile/2.2/ccache/language/cps.go
/usr/lib64/guile/2.2/ccache/language/cps/closure-conversion.go
/usr/lib64/guile/2.2/ccache/language/cps/compile-bytecode.go
/usr/lib64/guile/2.2/ccache/language/cps/constructors.go
/usr/lib64/guile/2.2/ccache/language/cps/contification.go
/usr/lib64/guile/2.2/ccache/language/cps/cse.go
/usr/lib64/guile/2.2/ccache/language/cps/dce.go
/usr/lib64/guile/2.2/ccache/language/cps/effects-analysis.go
/usr/lib64/guile/2.2/ccache/language/cps/elide-values.go
/usr/lib64/guile/2.2/ccache/language/cps/handle-interrupts.go
/usr/lib64/guile/2.2/ccache/language/cps/intmap.go
/usr/lib64/guile/2.2/ccache/language/cps/intset.go
/usr/lib64/guile/2.2/ccache/language/cps/licm.go
/usr/lib64/guile/2.2/ccache/language/cps/optimize.go
/usr/lib64/guile/2.2/ccache/language/cps/peel-loops.go
/usr/lib64/guile/2.2/ccache/language/cps/primitives.go
/usr/lib64/guile/2.2/ccache/language/cps/prune-bailouts.go
/usr/lib64/guile/2.2/ccache/language/cps/prune-top-level-scopes.go
/usr/lib64/guile/2.2/ccache/language/cps/reify-primitives.go
/usr/lib64/guile/2.2/ccache/language/cps/renumber.go
/usr/lib64/guile/2.2/ccache/language/cps/rotate-loops.go
/usr/lib64/guile/2.2/ccache/language/cps/self-references.go
/usr/lib64/guile/2.2/ccache/language/cps/simplify.go
/usr/lib64/guile/2.2/ccache/language/cps/slot-allocation.go
/usr/lib64/guile/2.2/ccache/language/cps/spec.go
/usr/lib64/guile/2.2/ccache/language/cps/specialize-numbers.go
/usr/lib64/guile/2.2/ccache/language/cps/specialize-primcalls.go
/usr/lib64/guile/2.2/ccache/language/cps/split-rec.go
/usr/lib64/guile/2.2/ccache/language/cps/type-checks.go
/usr/lib64/guile/2.2/ccache/language/cps/type-fold.go
/usr/lib64/guile/2.2/ccache/language/cps/types.go
/usr/lib64/guile/2.2/ccache/language/cps/utils.go
/usr/lib64/guile/2.2/ccache/language/cps/verify.go
/usr/lib64/guile/2.2/ccache/language/cps/with-cps.go
/usr/lib64/guile/2.2/ccache/language/ecmascript/array.go
/usr/lib64/guile/2.2/ccache/language/ecmascript/base.go
/usr/lib64/guile/2.2/ccache/language/ecmascript/compile-tree-il.go
/usr/lib64/guile/2.2/ccache/language/ecmascript/function.go
/usr/lib64/guile/2.2/ccache/language/ecmascript/impl.go
/usr/lib64/guile/2.2/ccache/language/ecmascript/parse.go
/usr/lib64/guile/2.2/ccache/language/ecmascript/spec.go
/usr/lib64/guile/2.2/ccache/language/ecmascript/tokenize.go
/usr/lib64/guile/2.2/ccache/language/elisp/bindings.go
/usr/lib64/guile/2.2/ccache/language/elisp/boot.go
/usr/lib64/guile/2.2/ccache/language/elisp/compile-tree-il.go
/usr/lib64/guile/2.2/ccache/language/elisp/falias.go
/usr/lib64/guile/2.2/ccache/language/elisp/lexer.go
/usr/lib64/guile/2.2/ccache/language/elisp/parser.go
/usr/lib64/guile/2.2/ccache/language/elisp/runtime.go
/usr/lib64/guile/2.2/ccache/language/elisp/runtime/function-slot.go
/usr/lib64/guile/2.2/ccache/language/elisp/runtime/value-slot.go
/usr/lib64/guile/2.2/ccache/language/elisp/spec.go
/usr/lib64/guile/2.2/ccache/language/scheme/compile-tree-il.go
/usr/lib64/guile/2.2/ccache/language/scheme/decompile-tree-il.go
/usr/lib64/guile/2.2/ccache/language/scheme/spec.go
/usr/lib64/guile/2.2/ccache/language/tree-il.go
/usr/lib64/guile/2.2/ccache/language/tree-il/analyze.go
/usr/lib64/guile/2.2/ccache/language/tree-il/canonicalize.go
/usr/lib64/guile/2.2/ccache/language/tree-il/compile-cps.go
/usr/lib64/guile/2.2/ccache/language/tree-il/debug.go
/usr/lib64/guile/2.2/ccache/language/tree-il/effects.go
/usr/lib64/guile/2.2/ccache/language/tree-il/fix-letrec.go
/usr/lib64/guile/2.2/ccache/language/tree-il/optimize.go
/usr/lib64/guile/2.2/ccache/language/tree-il/peval.go
/usr/lib64/guile/2.2/ccache/language/tree-il/primitives.go
/usr/lib64/guile/2.2/ccache/language/tree-il/spec.go
/usr/lib64/guile/2.2/ccache/language/value/spec.go
/usr/lib64/guile/2.2/ccache/oop/goops.go
/usr/lib64/guile/2.2/ccache/oop/goops/accessors.go
/usr/lib64/guile/2.2/ccache/oop/goops/active-slot.go
/usr/lib64/guile/2.2/ccache/oop/goops/composite-slot.go
/usr/lib64/guile/2.2/ccache/oop/goops/describe.go
/usr/lib64/guile/2.2/ccache/oop/goops/internal.go
/usr/lib64/guile/2.2/ccache/oop/goops/save.go
/usr/lib64/guile/2.2/ccache/oop/goops/simple.go
/usr/lib64/guile/2.2/ccache/oop/goops/stklos.go
/usr/lib64/guile/2.2/ccache/rnrs.go
/usr/lib64/guile/2.2/ccache/rnrs/arithmetic/bitwise.go
/usr/lib64/guile/2.2/ccache/rnrs/arithmetic/fixnums.go
/usr/lib64/guile/2.2/ccache/rnrs/arithmetic/flonums.go
/usr/lib64/guile/2.2/ccache/rnrs/base.go
/usr/lib64/guile/2.2/ccache/rnrs/bytevectors.go
/usr/lib64/guile/2.2/ccache/rnrs/conditions.go
/usr/lib64/guile/2.2/ccache/rnrs/control.go
/usr/lib64/guile/2.2/ccache/rnrs/enums.go
/usr/lib64/guile/2.2/ccache/rnrs/eval.go
/usr/lib64/guile/2.2/ccache/rnrs/exceptions.go
/usr/lib64/guile/2.2/ccache/rnrs/files.go
/usr/lib64/guile/2.2/ccache/rnrs/hashtables.go
/usr/lib64/guile/2.2/ccache/rnrs/io/ports.go
/usr/lib64/guile/2.2/ccache/rnrs/io/simple.go
/usr/lib64/guile/2.2/ccache/rnrs/lists.go
/usr/lib64/guile/2.2/ccache/rnrs/mutable-pairs.go
/usr/lib64/guile/2.2/ccache/rnrs/mutable-strings.go
/usr/lib64/guile/2.2/ccache/rnrs/programs.go
/usr/lib64/guile/2.2/ccache/rnrs/r5rs.go
/usr/lib64/guile/2.2/ccache/rnrs/records/inspection.go
/usr/lib64/guile/2.2/ccache/rnrs/records/procedural.go
/usr/lib64/guile/2.2/ccache/rnrs/records/syntactic.go
/usr/lib64/guile/2.2/ccache/rnrs/sorting.go
/usr/lib64/guile/2.2/ccache/rnrs/syntax-case.go
/usr/lib64/guile/2.2/ccache/rnrs/unicode.go
/usr/lib64/guile/2.2/ccache/scripts/api-diff.go
/usr/lib64/guile/2.2/ccache/scripts/autofrisk.go
/usr/lib64/guile/2.2/ccache/scripts/compile.go
/usr/lib64/guile/2.2/ccache/scripts/disassemble.go
/usr/lib64/guile/2.2/ccache/scripts/display-commentary.go
/usr/lib64/guile/2.2/ccache/scripts/doc-snarf.go
/usr/lib64/guile/2.2/ccache/scripts/frisk.go
/usr/lib64/guile/2.2/ccache/scripts/generate-autoload.go
/usr/lib64/guile/2.2/ccache/scripts/help.go
/usr/lib64/guile/2.2/ccache/scripts/lint.go
/usr/lib64/guile/2.2/ccache/scripts/list.go
/usr/lib64/guile/2.2/ccache/scripts/punify.go
/usr/lib64/guile/2.2/ccache/scripts/read-rfc822.go
/usr/lib64/guile/2.2/ccache/scripts/read-scheme-source.go
/usr/lib64/guile/2.2/ccache/scripts/read-text-outline.go
/usr/lib64/guile/2.2/ccache/scripts/scan-api.go
/usr/lib64/guile/2.2/ccache/scripts/snarf-check-and-output-texi.go
/usr/lib64/guile/2.2/ccache/scripts/snarf-guile-m4-docs.go
/usr/lib64/guile/2.2/ccache/scripts/summarize-guile-TODO.go
/usr/lib64/guile/2.2/ccache/scripts/use2dot.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-1.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-10.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-11.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-111.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-13.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-14.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-16.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-17.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-18.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-19.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-2.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-26.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-27.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-28.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-31.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-34.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-35.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-37.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-38.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-39.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-4.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-4/gnu.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-41.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-42.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-43.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-45.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-6.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-60.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-64.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-67.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-69.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-71.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-8.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-88.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-9.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-9/gnu.go
/usr/lib64/guile/2.2/ccache/srfi/srfi-98.go
/usr/lib64/guile/2.2/ccache/statprof.go
/usr/lib64/guile/2.2/ccache/sxml/apply-templates.go
/usr/lib64/guile/2.2/ccache/sxml/fold.go
/usr/lib64/guile/2.2/ccache/sxml/match.go
/usr/lib64/guile/2.2/ccache/sxml/simple.go
/usr/lib64/guile/2.2/ccache/sxml/ssax.go
/usr/lib64/guile/2.2/ccache/sxml/ssax/input-parse.go
/usr/lib64/guile/2.2/ccache/sxml/transform.go
/usr/lib64/guile/2.2/ccache/sxml/xpath.go
/usr/lib64/guile/2.2/ccache/system/base/ck.go
/usr/lib64/guile/2.2/ccache/system/base/compile.go
/usr/lib64/guile/2.2/ccache/system/base/lalr.go
/usr/lib64/guile/2.2/ccache/system/base/language.go
/usr/lib64/guile/2.2/ccache/system/base/message.go
/usr/lib64/guile/2.2/ccache/system/base/pmatch.go
/usr/lib64/guile/2.2/ccache/system/base/syntax.go
/usr/lib64/guile/2.2/ccache/system/base/target.go
/usr/lib64/guile/2.2/ccache/system/base/types.go
/usr/lib64/guile/2.2/ccache/system/foreign-object.go
/usr/lib64/guile/2.2/ccache/system/foreign.go
/usr/lib64/guile/2.2/ccache/system/repl/command.go
/usr/lib64/guile/2.2/ccache/system/repl/common.go
/usr/lib64/guile/2.2/ccache/system/repl/coop-server.go
/usr/lib64/guile/2.2/ccache/system/repl/debug.go
/usr/lib64/guile/2.2/ccache/system/repl/error-handling.go
/usr/lib64/guile/2.2/ccache/system/repl/repl.go
/usr/lib64/guile/2.2/ccache/system/repl/server.go
/usr/lib64/guile/2.2/ccache/system/syntax.go
/usr/lib64/guile/2.2/ccache/system/vm/assembler.go
/usr/lib64/guile/2.2/ccache/system/vm/coverage.go
/usr/lib64/guile/2.2/ccache/system/vm/debug.go
/usr/lib64/guile/2.2/ccache/system/vm/disassembler.go
/usr/lib64/guile/2.2/ccache/system/vm/dwarf.go
/usr/lib64/guile/2.2/ccache/system/vm/elf.go
/usr/lib64/guile/2.2/ccache/system/vm/frame.go
/usr/lib64/guile/2.2/ccache/system/vm/inspect.go
/usr/lib64/guile/2.2/ccache/system/vm/linker.go
/usr/lib64/guile/2.2/ccache/system/vm/loader.go
/usr/lib64/guile/2.2/ccache/system/vm/program.go
/usr/lib64/guile/2.2/ccache/system/vm/trace.go
/usr/lib64/guile/2.2/ccache/system/vm/trap-state.go
/usr/lib64/guile/2.2/ccache/system/vm/traps.go
/usr/lib64/guile/2.2/ccache/system/vm/vm.go
/usr/lib64/guile/2.2/ccache/system/xref.go
/usr/lib64/guile/2.2/ccache/texinfo.go
/usr/lib64/guile/2.2/ccache/texinfo/docbook.go
/usr/lib64/guile/2.2/ccache/texinfo/html.go
/usr/lib64/guile/2.2/ccache/texinfo/indexing.go
/usr/lib64/guile/2.2/ccache/texinfo/plain-text.go
/usr/lib64/guile/2.2/ccache/texinfo/reflection.go
/usr/lib64/guile/2.2/ccache/texinfo/serialize.go
/usr/lib64/guile/2.2/ccache/texinfo/string-utils.go
/usr/lib64/guile/2.2/ccache/web/client.go
/usr/lib64/guile/2.2/ccache/web/http.go
/usr/lib64/guile/2.2/ccache/web/request.go
/usr/lib64/guile/2.2/ccache/web/response.go
/usr/lib64/guile/2.2/ccache/web/server.go
/usr/lib64/guile/2.2/ccache/web/server/http.go
/usr/lib64/guile/2.2/ccache/web/uri.go

%files bin
%defattr(-,root,root,-)
/usr/bin/guild
/usr/bin/guile
/usr/bin/guile-config
/usr/bin/guile-snarf
/usr/bin/guile-tools

%files data
%defattr(-,root,root,-)
/usr/share/guile/2.2/guile-procedures.txt
/usr/share/guile/2.2/ice-9/and-let-star.scm
/usr/share/guile/2.2/ice-9/arrays.scm
/usr/share/guile/2.2/ice-9/atomic.scm
/usr/share/guile/2.2/ice-9/binary-ports.scm
/usr/share/guile/2.2/ice-9/boot-9.scm
/usr/share/guile/2.2/ice-9/buffered-input.scm
/usr/share/guile/2.2/ice-9/calling.scm
/usr/share/guile/2.2/ice-9/channel.scm
/usr/share/guile/2.2/ice-9/command-line.scm
/usr/share/guile/2.2/ice-9/common-list.scm
/usr/share/guile/2.2/ice-9/control.scm
/usr/share/guile/2.2/ice-9/curried-definitions.scm
/usr/share/guile/2.2/ice-9/debug.scm
/usr/share/guile/2.2/ice-9/deprecated.scm
/usr/share/guile/2.2/ice-9/documentation.scm
/usr/share/guile/2.2/ice-9/eval-string.scm
/usr/share/guile/2.2/ice-9/eval.scm
/usr/share/guile/2.2/ice-9/expect.scm
/usr/share/guile/2.2/ice-9/fdes-finalizers.scm
/usr/share/guile/2.2/ice-9/format.scm
/usr/share/guile/2.2/ice-9/ftw.scm
/usr/share/guile/2.2/ice-9/futures.scm
/usr/share/guile/2.2/ice-9/gap-buffer.scm
/usr/share/guile/2.2/ice-9/getopt-long.scm
/usr/share/guile/2.2/ice-9/hash-table.scm
/usr/share/guile/2.2/ice-9/hcons.scm
/usr/share/guile/2.2/ice-9/history.scm
/usr/share/guile/2.2/ice-9/i18n.scm
/usr/share/guile/2.2/ice-9/iconv.scm
/usr/share/guile/2.2/ice-9/lineio.scm
/usr/share/guile/2.2/ice-9/list.scm
/usr/share/guile/2.2/ice-9/local-eval.scm
/usr/share/guile/2.2/ice-9/ls.scm
/usr/share/guile/2.2/ice-9/mapping.scm
/usr/share/guile/2.2/ice-9/match.scm
/usr/share/guile/2.2/ice-9/match.upstream.scm
/usr/share/guile/2.2/ice-9/networking.scm
/usr/share/guile/2.2/ice-9/null.scm
/usr/share/guile/2.2/ice-9/occam-channel.scm
/usr/share/guile/2.2/ice-9/optargs.scm
/usr/share/guile/2.2/ice-9/peg.scm
/usr/share/guile/2.2/ice-9/peg/cache.scm
/usr/share/guile/2.2/ice-9/peg/codegen.scm
/usr/share/guile/2.2/ice-9/peg/simplify-tree.scm
/usr/share/guile/2.2/ice-9/peg/string-peg.scm
/usr/share/guile/2.2/ice-9/peg/using-parsers.scm
/usr/share/guile/2.2/ice-9/poe.scm
/usr/share/guile/2.2/ice-9/poll.scm
/usr/share/guile/2.2/ice-9/popen.scm
/usr/share/guile/2.2/ice-9/ports.scm
/usr/share/guile/2.2/ice-9/posix.scm
/usr/share/guile/2.2/ice-9/pretty-print.scm
/usr/share/guile/2.2/ice-9/psyntax-pp.scm
/usr/share/guile/2.2/ice-9/psyntax.scm
/usr/share/guile/2.2/ice-9/q.scm
/usr/share/guile/2.2/ice-9/quasisyntax.scm
/usr/share/guile/2.2/ice-9/r5rs.scm
/usr/share/guile/2.2/ice-9/r6rs-libraries.scm
/usr/share/guile/2.2/ice-9/rdelim.scm
/usr/share/guile/2.2/ice-9/readline.scm
/usr/share/guile/2.2/ice-9/receive.scm
/usr/share/guile/2.2/ice-9/regex.scm
/usr/share/guile/2.2/ice-9/runq.scm
/usr/share/guile/2.2/ice-9/rw.scm
/usr/share/guile/2.2/ice-9/safe-r5rs.scm
/usr/share/guile/2.2/ice-9/safe.scm
/usr/share/guile/2.2/ice-9/sandbox.scm
/usr/share/guile/2.2/ice-9/save-stack.scm
/usr/share/guile/2.2/ice-9/scm-style-repl.scm
/usr/share/guile/2.2/ice-9/serialize.scm
/usr/share/guile/2.2/ice-9/session.scm
/usr/share/guile/2.2/ice-9/slib.scm
/usr/share/guile/2.2/ice-9/stack-catch.scm
/usr/share/guile/2.2/ice-9/streams.scm
/usr/share/guile/2.2/ice-9/string-fun.scm
/usr/share/guile/2.2/ice-9/suspendable-ports.scm
/usr/share/guile/2.2/ice-9/syncase.scm
/usr/share/guile/2.2/ice-9/textual-ports.scm
/usr/share/guile/2.2/ice-9/threads.scm
/usr/share/guile/2.2/ice-9/time.scm
/usr/share/guile/2.2/ice-9/top-repl.scm
/usr/share/guile/2.2/ice-9/unicode.scm
/usr/share/guile/2.2/ice-9/vlist.scm
/usr/share/guile/2.2/ice-9/weak-vector.scm
/usr/share/guile/2.2/language/brainfuck/compile-scheme.scm
/usr/share/guile/2.2/language/brainfuck/compile-tree-il.scm
/usr/share/guile/2.2/language/brainfuck/parse.scm
/usr/share/guile/2.2/language/brainfuck/spec.scm
/usr/share/guile/2.2/language/bytecode.scm
/usr/share/guile/2.2/language/bytecode/spec.scm
/usr/share/guile/2.2/language/cps.scm
/usr/share/guile/2.2/language/cps/closure-conversion.scm
/usr/share/guile/2.2/language/cps/compile-bytecode.scm
/usr/share/guile/2.2/language/cps/constructors.scm
/usr/share/guile/2.2/language/cps/contification.scm
/usr/share/guile/2.2/language/cps/cse.scm
/usr/share/guile/2.2/language/cps/dce.scm
/usr/share/guile/2.2/language/cps/effects-analysis.scm
/usr/share/guile/2.2/language/cps/elide-values.scm
/usr/share/guile/2.2/language/cps/handle-interrupts.scm
/usr/share/guile/2.2/language/cps/intmap.scm
/usr/share/guile/2.2/language/cps/intset.scm
/usr/share/guile/2.2/language/cps/licm.scm
/usr/share/guile/2.2/language/cps/optimize.scm
/usr/share/guile/2.2/language/cps/peel-loops.scm
/usr/share/guile/2.2/language/cps/primitives.scm
/usr/share/guile/2.2/language/cps/prune-bailouts.scm
/usr/share/guile/2.2/language/cps/prune-top-level-scopes.scm
/usr/share/guile/2.2/language/cps/reify-primitives.scm
/usr/share/guile/2.2/language/cps/renumber.scm
/usr/share/guile/2.2/language/cps/rotate-loops.scm
/usr/share/guile/2.2/language/cps/self-references.scm
/usr/share/guile/2.2/language/cps/simplify.scm
/usr/share/guile/2.2/language/cps/slot-allocation.scm
/usr/share/guile/2.2/language/cps/spec.scm
/usr/share/guile/2.2/language/cps/specialize-numbers.scm
/usr/share/guile/2.2/language/cps/specialize-primcalls.scm
/usr/share/guile/2.2/language/cps/split-rec.scm
/usr/share/guile/2.2/language/cps/type-checks.scm
/usr/share/guile/2.2/language/cps/type-fold.scm
/usr/share/guile/2.2/language/cps/types.scm
/usr/share/guile/2.2/language/cps/utils.scm
/usr/share/guile/2.2/language/cps/verify.scm
/usr/share/guile/2.2/language/cps/with-cps.scm
/usr/share/guile/2.2/language/ecmascript/array.scm
/usr/share/guile/2.2/language/ecmascript/base.scm
/usr/share/guile/2.2/language/ecmascript/compile-tree-il.scm
/usr/share/guile/2.2/language/ecmascript/function.scm
/usr/share/guile/2.2/language/ecmascript/impl.scm
/usr/share/guile/2.2/language/ecmascript/parse.scm
/usr/share/guile/2.2/language/ecmascript/spec.scm
/usr/share/guile/2.2/language/ecmascript/tokenize.scm
/usr/share/guile/2.2/language/elisp/bindings.scm
/usr/share/guile/2.2/language/elisp/boot.el
/usr/share/guile/2.2/language/elisp/compile-tree-il.scm
/usr/share/guile/2.2/language/elisp/falias.scm
/usr/share/guile/2.2/language/elisp/lexer.scm
/usr/share/guile/2.2/language/elisp/parser.scm
/usr/share/guile/2.2/language/elisp/runtime.scm
/usr/share/guile/2.2/language/elisp/runtime/function-slot.scm
/usr/share/guile/2.2/language/elisp/runtime/value-slot.scm
/usr/share/guile/2.2/language/elisp/spec.scm
/usr/share/guile/2.2/language/scheme/compile-tree-il.scm
/usr/share/guile/2.2/language/scheme/decompile-tree-il.scm
/usr/share/guile/2.2/language/scheme/spec.scm
/usr/share/guile/2.2/language/tree-il.scm
/usr/share/guile/2.2/language/tree-il/analyze.scm
/usr/share/guile/2.2/language/tree-il/canonicalize.scm
/usr/share/guile/2.2/language/tree-il/compile-cps.scm
/usr/share/guile/2.2/language/tree-il/debug.scm
/usr/share/guile/2.2/language/tree-il/effects.scm
/usr/share/guile/2.2/language/tree-il/fix-letrec.scm
/usr/share/guile/2.2/language/tree-il/optimize.scm
/usr/share/guile/2.2/language/tree-il/peval.scm
/usr/share/guile/2.2/language/tree-il/primitives.scm
/usr/share/guile/2.2/language/tree-il/spec.scm
/usr/share/guile/2.2/language/value/spec.scm
/usr/share/guile/2.2/oop/goops.scm
/usr/share/guile/2.2/oop/goops/accessors.scm
/usr/share/guile/2.2/oop/goops/active-slot.scm
/usr/share/guile/2.2/oop/goops/composite-slot.scm
/usr/share/guile/2.2/oop/goops/describe.scm
/usr/share/guile/2.2/oop/goops/internal.scm
/usr/share/guile/2.2/oop/goops/save.scm
/usr/share/guile/2.2/oop/goops/simple.scm
/usr/share/guile/2.2/oop/goops/stklos.scm
/usr/share/guile/2.2/rnrs.scm
/usr/share/guile/2.2/rnrs/arithmetic/bitwise.scm
/usr/share/guile/2.2/rnrs/arithmetic/fixnums.scm
/usr/share/guile/2.2/rnrs/arithmetic/flonums.scm
/usr/share/guile/2.2/rnrs/base.scm
/usr/share/guile/2.2/rnrs/bytevectors.scm
/usr/share/guile/2.2/rnrs/conditions.scm
/usr/share/guile/2.2/rnrs/control.scm
/usr/share/guile/2.2/rnrs/enums.scm
/usr/share/guile/2.2/rnrs/eval.scm
/usr/share/guile/2.2/rnrs/exceptions.scm
/usr/share/guile/2.2/rnrs/files.scm
/usr/share/guile/2.2/rnrs/hashtables.scm
/usr/share/guile/2.2/rnrs/io/ports.scm
/usr/share/guile/2.2/rnrs/io/simple.scm
/usr/share/guile/2.2/rnrs/lists.scm
/usr/share/guile/2.2/rnrs/mutable-pairs.scm
/usr/share/guile/2.2/rnrs/mutable-strings.scm
/usr/share/guile/2.2/rnrs/programs.scm
/usr/share/guile/2.2/rnrs/r5rs.scm
/usr/share/guile/2.2/rnrs/records/inspection.scm
/usr/share/guile/2.2/rnrs/records/procedural.scm
/usr/share/guile/2.2/rnrs/records/syntactic.scm
/usr/share/guile/2.2/rnrs/sorting.scm
/usr/share/guile/2.2/rnrs/syntax-case.scm
/usr/share/guile/2.2/rnrs/unicode.scm
/usr/share/guile/2.2/scripts/api-diff.scm
/usr/share/guile/2.2/scripts/autofrisk.scm
/usr/share/guile/2.2/scripts/compile.scm
/usr/share/guile/2.2/scripts/disassemble.scm
/usr/share/guile/2.2/scripts/display-commentary.scm
/usr/share/guile/2.2/scripts/doc-snarf.scm
/usr/share/guile/2.2/scripts/frisk.scm
/usr/share/guile/2.2/scripts/generate-autoload.scm
/usr/share/guile/2.2/scripts/help.scm
/usr/share/guile/2.2/scripts/lint.scm
/usr/share/guile/2.2/scripts/list.scm
/usr/share/guile/2.2/scripts/punify.scm
/usr/share/guile/2.2/scripts/read-rfc822.scm
/usr/share/guile/2.2/scripts/read-scheme-source.scm
/usr/share/guile/2.2/scripts/read-text-outline.scm
/usr/share/guile/2.2/scripts/scan-api.scm
/usr/share/guile/2.2/scripts/snarf-check-and-output-texi.scm
/usr/share/guile/2.2/scripts/snarf-guile-m4-docs.scm
/usr/share/guile/2.2/scripts/summarize-guile-TODO.scm
/usr/share/guile/2.2/scripts/use2dot.scm
/usr/share/guile/2.2/srfi/srfi-1.scm
/usr/share/guile/2.2/srfi/srfi-10.scm
/usr/share/guile/2.2/srfi/srfi-11.scm
/usr/share/guile/2.2/srfi/srfi-111.scm
/usr/share/guile/2.2/srfi/srfi-13.scm
/usr/share/guile/2.2/srfi/srfi-14.scm
/usr/share/guile/2.2/srfi/srfi-16.scm
/usr/share/guile/2.2/srfi/srfi-17.scm
/usr/share/guile/2.2/srfi/srfi-18.scm
/usr/share/guile/2.2/srfi/srfi-19.scm
/usr/share/guile/2.2/srfi/srfi-2.scm
/usr/share/guile/2.2/srfi/srfi-26.scm
/usr/share/guile/2.2/srfi/srfi-27.scm
/usr/share/guile/2.2/srfi/srfi-28.scm
/usr/share/guile/2.2/srfi/srfi-31.scm
/usr/share/guile/2.2/srfi/srfi-34.scm
/usr/share/guile/2.2/srfi/srfi-35.scm
/usr/share/guile/2.2/srfi/srfi-37.scm
/usr/share/guile/2.2/srfi/srfi-38.scm
/usr/share/guile/2.2/srfi/srfi-39.scm
/usr/share/guile/2.2/srfi/srfi-4.scm
/usr/share/guile/2.2/srfi/srfi-4/gnu.scm
/usr/share/guile/2.2/srfi/srfi-41.scm
/usr/share/guile/2.2/srfi/srfi-42.scm
/usr/share/guile/2.2/srfi/srfi-42/ec.scm
/usr/share/guile/2.2/srfi/srfi-43.scm
/usr/share/guile/2.2/srfi/srfi-45.scm
/usr/share/guile/2.2/srfi/srfi-6.scm
/usr/share/guile/2.2/srfi/srfi-60.scm
/usr/share/guile/2.2/srfi/srfi-64.scm
/usr/share/guile/2.2/srfi/srfi-64/testing.scm
/usr/share/guile/2.2/srfi/srfi-67.scm
/usr/share/guile/2.2/srfi/srfi-67/compare.scm
/usr/share/guile/2.2/srfi/srfi-69.scm
/usr/share/guile/2.2/srfi/srfi-71.scm
/usr/share/guile/2.2/srfi/srfi-8.scm
/usr/share/guile/2.2/srfi/srfi-88.scm
/usr/share/guile/2.2/srfi/srfi-9.scm
/usr/share/guile/2.2/srfi/srfi-9/gnu.scm
/usr/share/guile/2.2/srfi/srfi-98.scm
/usr/share/guile/2.2/statprof.scm
/usr/share/guile/2.2/sxml/apply-templates.scm
/usr/share/guile/2.2/sxml/fold.scm
/usr/share/guile/2.2/sxml/match.scm
/usr/share/guile/2.2/sxml/simple.scm
/usr/share/guile/2.2/sxml/ssax.scm
/usr/share/guile/2.2/sxml/ssax/input-parse.scm
/usr/share/guile/2.2/sxml/sxml-match.ss
/usr/share/guile/2.2/sxml/transform.scm
/usr/share/guile/2.2/sxml/upstream/SSAX.scm
/usr/share/guile/2.2/sxml/upstream/SXML-tree-trans.scm
/usr/share/guile/2.2/sxml/upstream/SXPath-old.scm
/usr/share/guile/2.2/sxml/upstream/assert.scm
/usr/share/guile/2.2/sxml/upstream/input-parse.scm
/usr/share/guile/2.2/sxml/xpath.scm
/usr/share/guile/2.2/system/base/ck.scm
/usr/share/guile/2.2/system/base/compile.scm
/usr/share/guile/2.2/system/base/lalr.scm
/usr/share/guile/2.2/system/base/lalr.upstream.scm
/usr/share/guile/2.2/system/base/language.scm
/usr/share/guile/2.2/system/base/message.scm
/usr/share/guile/2.2/system/base/pmatch.scm
/usr/share/guile/2.2/system/base/syntax.scm
/usr/share/guile/2.2/system/base/target.scm
/usr/share/guile/2.2/system/base/types.scm
/usr/share/guile/2.2/system/foreign-object.scm
/usr/share/guile/2.2/system/foreign.scm
/usr/share/guile/2.2/system/repl/command.scm
/usr/share/guile/2.2/system/repl/common.scm
/usr/share/guile/2.2/system/repl/coop-server.scm
/usr/share/guile/2.2/system/repl/debug.scm
/usr/share/guile/2.2/system/repl/describe.scm
/usr/share/guile/2.2/system/repl/error-handling.scm
/usr/share/guile/2.2/system/repl/repl.scm
/usr/share/guile/2.2/system/repl/server.scm
/usr/share/guile/2.2/system/syntax.scm
/usr/share/guile/2.2/system/vm/assembler.scm
/usr/share/guile/2.2/system/vm/coverage.scm
/usr/share/guile/2.2/system/vm/debug.scm
/usr/share/guile/2.2/system/vm/disassembler.scm
/usr/share/guile/2.2/system/vm/dwarf.scm
/usr/share/guile/2.2/system/vm/elf.scm
/usr/share/guile/2.2/system/vm/frame.scm
/usr/share/guile/2.2/system/vm/inspect.scm
/usr/share/guile/2.2/system/vm/linker.scm
/usr/share/guile/2.2/system/vm/loader.scm
/usr/share/guile/2.2/system/vm/program.scm
/usr/share/guile/2.2/system/vm/trace.scm
/usr/share/guile/2.2/system/vm/trap-state.scm
/usr/share/guile/2.2/system/vm/traps.scm
/usr/share/guile/2.2/system/vm/vm.scm
/usr/share/guile/2.2/system/xref.scm
/usr/share/guile/2.2/texinfo.scm
/usr/share/guile/2.2/texinfo/docbook.scm
/usr/share/guile/2.2/texinfo/html.scm
/usr/share/guile/2.2/texinfo/indexing.scm
/usr/share/guile/2.2/texinfo/plain-text.scm
/usr/share/guile/2.2/texinfo/reflection.scm
/usr/share/guile/2.2/texinfo/serialize.scm
/usr/share/guile/2.2/texinfo/string-utils.scm
/usr/share/guile/2.2/web/client.scm
/usr/share/guile/2.2/web/http.scm
/usr/share/guile/2.2/web/request.scm
/usr/share/guile/2.2/web/response.scm
/usr/share/guile/2.2/web/server.scm
/usr/share/guile/2.2/web/server/http.scm
/usr/share/guile/2.2/web/uri.scm

%files dev
%defattr(-,root,root,-)
/usr/include/guile/2.2/libguile.h
/usr/include/guile/2.2/libguile/__scm.h
/usr/include/guile/2.2/libguile/alist.h
/usr/include/guile/2.2/libguile/array-handle.h
/usr/include/guile/2.2/libguile/array-map.h
/usr/include/guile/2.2/libguile/arrays.h
/usr/include/guile/2.2/libguile/async.h
/usr/include/guile/2.2/libguile/atomic.h
/usr/include/guile/2.2/libguile/backtrace.h
/usr/include/guile/2.2/libguile/bdw-gc.h
/usr/include/guile/2.2/libguile/bitvectors.h
/usr/include/guile/2.2/libguile/boolean.h
/usr/include/guile/2.2/libguile/bytevectors.h
/usr/include/guile/2.2/libguile/chars.h
/usr/include/guile/2.2/libguile/continuations.h
/usr/include/guile/2.2/libguile/control.h
/usr/include/guile/2.2/libguile/debug-malloc.h
/usr/include/guile/2.2/libguile/debug.h
/usr/include/guile/2.2/libguile/deprecated.h
/usr/include/guile/2.2/libguile/deprecation.h
/usr/include/guile/2.2/libguile/dynl.h
/usr/include/guile/2.2/libguile/dynstack.h
/usr/include/guile/2.2/libguile/dynwind.h
/usr/include/guile/2.2/libguile/eq.h
/usr/include/guile/2.2/libguile/error.h
/usr/include/guile/2.2/libguile/eval.h
/usr/include/guile/2.2/libguile/evalext.h
/usr/include/guile/2.2/libguile/expand.h
/usr/include/guile/2.2/libguile/extensions.h
/usr/include/guile/2.2/libguile/fdes-finalizers.h
/usr/include/guile/2.2/libguile/feature.h
/usr/include/guile/2.2/libguile/filesys.h
/usr/include/guile/2.2/libguile/finalizers.h
/usr/include/guile/2.2/libguile/fluids.h
/usr/include/guile/2.2/libguile/foreign-object.h
/usr/include/guile/2.2/libguile/foreign.h
/usr/include/guile/2.2/libguile/fports.h
/usr/include/guile/2.2/libguile/frames.h
/usr/include/guile/2.2/libguile/gc-inline.h
/usr/include/guile/2.2/libguile/gc.h
/usr/include/guile/2.2/libguile/generalized-arrays.h
/usr/include/guile/2.2/libguile/generalized-vectors.h
/usr/include/guile/2.2/libguile/gettext.h
/usr/include/guile/2.2/libguile/goops.h
/usr/include/guile/2.2/libguile/gsubr.h
/usr/include/guile/2.2/libguile/guardians.h
/usr/include/guile/2.2/libguile/hash.h
/usr/include/guile/2.2/libguile/hashtab.h
/usr/include/guile/2.2/libguile/hooks.h
/usr/include/guile/2.2/libguile/i18n.h
/usr/include/guile/2.2/libguile/init.h
/usr/include/guile/2.2/libguile/inline.h
/usr/include/guile/2.2/libguile/instructions.h
/usr/include/guile/2.2/libguile/ioext.h
/usr/include/guile/2.2/libguile/iselect.h
/usr/include/guile/2.2/libguile/keywords.h
/usr/include/guile/2.2/libguile/list.h
/usr/include/guile/2.2/libguile/load.h
/usr/include/guile/2.2/libguile/loader.h
/usr/include/guile/2.2/libguile/macros.h
/usr/include/guile/2.2/libguile/mallocs.h
/usr/include/guile/2.2/libguile/memoize.h
/usr/include/guile/2.2/libguile/modules.h
/usr/include/guile/2.2/libguile/net_db.h
/usr/include/guile/2.2/libguile/null-threads.h
/usr/include/guile/2.2/libguile/numbers.h
/usr/include/guile/2.2/libguile/objprop.h
/usr/include/guile/2.2/libguile/options.h
/usr/include/guile/2.2/libguile/pairs.h
/usr/include/guile/2.2/libguile/poll.h
/usr/include/guile/2.2/libguile/ports.h
/usr/include/guile/2.2/libguile/posix.h
/usr/include/guile/2.2/libguile/print.h
/usr/include/guile/2.2/libguile/procprop.h
/usr/include/guile/2.2/libguile/procs.h
/usr/include/guile/2.2/libguile/programs.h
/usr/include/guile/2.2/libguile/promises.h
/usr/include/guile/2.2/libguile/pthread-threads.h
/usr/include/guile/2.2/libguile/r6rs-ports.h
/usr/include/guile/2.2/libguile/random.h
/usr/include/guile/2.2/libguile/rdelim.h
/usr/include/guile/2.2/libguile/read.h
/usr/include/guile/2.2/libguile/regex-posix.h
/usr/include/guile/2.2/libguile/rw.h
/usr/include/guile/2.2/libguile/scmconfig.h
/usr/include/guile/2.2/libguile/scmsigs.h
/usr/include/guile/2.2/libguile/script.h
/usr/include/guile/2.2/libguile/simpos.h
/usr/include/guile/2.2/libguile/smob.h
/usr/include/guile/2.2/libguile/snarf.h
/usr/include/guile/2.2/libguile/socket.h
/usr/include/guile/2.2/libguile/sort.h
/usr/include/guile/2.2/libguile/srcprop.h
/usr/include/guile/2.2/libguile/srfi-1.h
/usr/include/guile/2.2/libguile/srfi-13.h
/usr/include/guile/2.2/libguile/srfi-14.h
/usr/include/guile/2.2/libguile/srfi-4.h
/usr/include/guile/2.2/libguile/srfi-60.h
/usr/include/guile/2.2/libguile/stackchk.h
/usr/include/guile/2.2/libguile/stacks.h
/usr/include/guile/2.2/libguile/stime.h
/usr/include/guile/2.2/libguile/strings.h
/usr/include/guile/2.2/libguile/strorder.h
/usr/include/guile/2.2/libguile/strports.h
/usr/include/guile/2.2/libguile/struct.h
/usr/include/guile/2.2/libguile/symbols.h
/usr/include/guile/2.2/libguile/tags.h
/usr/include/guile/2.2/libguile/threads.h
/usr/include/guile/2.2/libguile/throw.h
/usr/include/guile/2.2/libguile/trees.h
/usr/include/guile/2.2/libguile/unicode.h
/usr/include/guile/2.2/libguile/uniform.h
/usr/include/guile/2.2/libguile/validate.h
/usr/include/guile/2.2/libguile/values.h
/usr/include/guile/2.2/libguile/variable.h
/usr/include/guile/2.2/libguile/vectors.h
/usr/include/guile/2.2/libguile/version.h
/usr/include/guile/2.2/libguile/vm-builtins.h
/usr/include/guile/2.2/libguile/vm-expand.h
/usr/include/guile/2.2/libguile/vm.h
/usr/include/guile/2.2/libguile/vports.h
/usr/include/guile/2.2/libguile/weak-set.h
/usr/include/guile/2.2/libguile/weak-table.h
/usr/include/guile/2.2/libguile/weak-vector.h
/usr/include/guile/2.2/readline.h
/usr/lib64/libguile-2.2.so
/usr/lib64/pkgconfig/guile-2.2.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/guile/2.2/extensions/guile-readline.so
/usr/lib64/guile/2.2/extensions/guile-readline.so.0
/usr/lib64/guile/2.2/extensions/guile-readline.so.0.0.0
/usr/lib64/libguile-2.2.so.1
/usr/lib64/libguile-2.2.so.1.4.1
/usr/lib64/libguile-2.2.so.1.4.1-gdb.scm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/guile/COPYING
/usr/share/package-licenses/guile/COPYING.LESSER
/usr/share/package-licenses/guile/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/guile.1
