import pymongo
from pymongo import MongoClient
import datetime
from MongoShopee import MongoDB
from pprint import pprint
client = MongoClient('localhost', 27017)
db = client.shopee_co_id

#db.createCollection('Category')
db.Category.insert_many([
    {'_id' : 'https://shopee.co.id/Kontrasepsi-cat.14780.14795',
    'level_1' : 'Kesehatan',
    'level_2' : 'Kontrasepsi',
    'status' : 1,
    'last_page' : 0
    },
    {'_id' : 'https://shopee.co.id/Suplemen-Makanan-cat.14780.14783',
    'level_1' : 'Kesehatan',
    'level_2' : 'Suplemen Makanan',
    'status' : 1,
    'last_page' : 0
    },
    {'_id' : 'https://shopee.co.id/Alat-Medis-cat.14780.14798',
    'level_1' : 'Kesehatan',
    'level_2' : 'Alat Medis',
    'status' : 1,
    'last_page' : 0
    },
    {'_id' : 'https://shopee.co.id/Perawatan-Diri-cat.14780.14789',
    'level_1' : 'Kesehatan',
    'level_2' : 'Perawatan Diri',
    'status' : 1,
    'last_page' : 0
    },
    {'_id' : 'https://shopee.co.id/Alat-Kecantikan-cat.14840.14932',
    'level_1' : 'Kecantikan',
    'level_2' : 'Alat Kecantikan',
    'status' : 1,
    'last_page' : 0
    },
    {'_id' : 'https://shopee.co.id/Alat-Rambut-cat.14840.18270',
    'level_1' : 'Kecantikan',
    'level_2' : 'Alat Rambut',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Perawatan-Tubuh-cat.14840.14854',
    'level_1' : 'Kecantikan',
    'level_2' : 'Perawatan Tubuh',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Kecantikan-Lainnya-cat.14840.14841',
    'level_1' : 'Kecantikan',
    'level_2' : 'Kecantikan Lainnya',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Kosmetik-Mata-cat.14840.14848',
    'level_1' : 'Kecantikan',
    'level_2' : 'Kosmetik Mata',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Perawatan-Kuku-cat.14840.18322',
    'level_1' : 'Kecantikan',
    'level_2' : 'Perawatan Kuku',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Perawatan-Pria-cat.14840.14864',
    'level_1' : 'Kecantikan',
    'level_2' : 'Perawatan Pria',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Kosmetik-Wajah-cat.14840.14845',
    'level_1' : 'Kecantikan',
    'level_2' : 'Kosmetik Wajah',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Perawatan-Rambut-cat.14840.14857',
    'level_1' : 'Kecantikan',
    'level_2' : 'Perawatan Rambut',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Parfum-cat.14840.14872',
    'level_1' : 'Kecantikan',
    'level_2' : 'Parfum',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Kosmetik-Bibir-cat.14840.14850',
    'level_1' : 'Kecantikan',
    'level_2' : 'Kosmetik Bibir',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Perawatan-Wajah-cat.14840.18309',
    'level_1' : 'Kecantikan',
    'level_2' : 'Perawatan Wajah',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Paket-Kecantikan-cat.14840.18335',
    'level_1' : 'Kecantikan',
    'level_2' : 'Paket Kecantikan',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Makanan-Bayi-cat.45.1269',
    'level_1' : 'Ibu Bayi',
    'level_2' : 'Makanan Bayi',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Perlengkapan-Mandi-Bayi-cat.45.12729',
    'level_1' : 'Ibu Bayi',
    'level_2' : 'Perlengkapan Mandi Bayi',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Perlengkapan-Makan-Bayi-cat.45.2838',
    'level_1' : 'Ibu Bayi',
    'level_2' : 'Perlengkapan Makan Bayi',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Perlengkapan-Tidur-Bayi-cat.45.2840',
    'level_1' : 'Ibu Bayi',
    'level_2' : 'Perlengkapan Tidur Bayi',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Perawatan-Bayi-cat.45.1261',
    'level_1' : 'Ibu Bayi',
    'level_2' : 'Perawatan Bayi',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Popok-Bayi-cat.45.1259',
    'level_1' : 'Ibu Bayi',
    'level_2' : 'Popok Bayi',
    'status' : 1,
    'last_page' : 0
    },{'_id' : 'https://shopee.co.id/Kebutuhan-Ibu-cat.45.15161',
    'level_1' : 'Ibu Bayi',
    'level_2' : 'Kebutuhan Ibu',
    'status' : 1,
    'last_page' : 0
    }
])
