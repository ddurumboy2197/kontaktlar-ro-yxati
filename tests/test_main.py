**Pytest uchun test kodı**
```python
import pytest
from kontaktlar import Kontaktlar

def test_kontaktlar_royxati():
    kontaktlar = Kontaktlar()
    kontaktlar.qosh("Ali", "99890123456")
    kontaktlar.qosh("Vali", "99890234567")
    assert kontaktlar.royxat() == [
        {"ism": "Ali", "telefon": "99890123456"},
        {"ism": "Vali", "telefon": "99890234567"}
    ]

def test_kontakt_qoshish():
    kontaktlar = Kontaktlar()
    kontaktlar.qosh("Ali", "99890123456")
    assert kontaktlar.royxat() == [
        {"ism": "Ali", "telefon": "99890123456"}
    ]

def test_kontakt_ochirish():
    kontaktlar = Kontaktlar()
    kontaktlar.qosh("Ali", "99890123456")
    kontaktlar.ochir("Ali")
    assert kontaktlar.royxat() == []

def test_kontakt_ochirish_builmaydi():
    kontaktlar = Kontaktlar()
    kontaktlar.qosh("Ali", "99890123456")
    kontaktlar.ochir("Vali")
    assert kontaktlar.royxat() == [
        {"ism": "Ali", "telefon": "99890123456"}
    ]
```

**Jest uchun test kodı**
```javascript
import Kontaktlar from './kontaktlar';

describe('Kontaktlar', () => {
  it('royxatni qaytaradi', () => {
    const kontaktlar = new Kontaktlar();
    kontaktlar.qosh('Ali', '99890123456');
    kontaktlar.qosh('Vali', '99890234567');
    expect(kontaktlar.royxat()).toEqual([
      { ism: 'Ali', telefon: '99890123456' },
      { ism: 'Vali', telefon: '99890234567' }
    ]);
  });

  it('kontakt qo\'shadi', () => {
    const kontaktlar = new Kontaktlar();
    kontaktlar.qosh('Ali', '99890123456');
    expect(kontaktlar.royxat()).toEqual([
      { ism: 'Ali', telefon: '99890123456' }
    ]);
  });

  it('kontakt o\'chiradi', () => {
    const kontaktlar = new Kontaktlar();
    kontaktlar.qosh('Ali', '99890123456');
    kontaktlar.ochir('Ali');
    expect(kontaktlar.royxat()).toEqual([]);
  });

  it('kontakt o\'chirishda muvaffaqiyatsizlik', () => {
    const kontaktlar = new Kontaktlar();
    kontaktlar.qosh('Ali', '99890123456');
    kontaktlar.ochir('Vali');
    expect(kontaktlar.royxat()).toEqual([
      { ism: 'Ali', telefon: '99890123456' }
    ]);
  });
});
```
