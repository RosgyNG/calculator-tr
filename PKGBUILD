pkgname='calculator-tr-git'
pkgver=0.1
pkgrel=1
pkgdesc="Basic turkish calculator writed in Python"
license=('GPL')
arch=('any')
makedepends=('python' 'python-pip')
source=("git+https://github.com/RosgyNG/calculator-tr.git")
md5sums=('SKIP')

prepare() {
	pip install pyinstaller
}

build() {
	cd "$srcdir/$pkgname"
	python -m PyInstaller --onefile calculator.py
}

package() {
	cd "$srcdir/$pkgname"
	mkdir -p "$pkgdir/usr/bin"
	cp "$srcdir/$pkgname/dist/calculator" "$pkgdir/usr/bin/calculator"
	chmod +x "$pkgdir/usr/bin/calculator"	
}
