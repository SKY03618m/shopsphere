SAMPLE_CATEGORIES = [
    {"name": "Electronics", "slug": "electronics", "icon": "laptop"},
    {"name": "Fashion", "slug": "fashion", "icon": "apparel"},
    {"name": "Home & Kitchen", "slug": "home-kitchen", "icon": "coffee"},
    {"name": "Books & Tech", "slug": "books-tech", "icon": "book"}
]

SAMPLE_PRODUCTS = [
    # Electronics
    {
        "category_slug": "electronics",
        "name": "NovaPulse Pro Smartwatch",
        "slug": "novapulse-pro-smartwatch",
        "description": "High-precision fitness and lifestyle smartwatch with AMOLED always-on display, 7-day battery life, and SpO2 tracking.",
        "price": 2999.0,
        "stock": 25,
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80"
    },
    {
        "category_slug": "electronics",
        "name": "AcousticZen ANC Headphones",
        "slug": "acousticzen-anc-headphones",
        "description": "Premium over-ear wireless headphones featuring active noise cancellation, transparency mode, and 40-hour playback.",
        "price": 4499.0,
        "stock": 18,
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80"
    },
    {
        "category_slug": "electronics",
        "name": "ApexKey RGB Mechanical Keyboard",
        "slug": "apexkey-rgb-mechanical-keyboard",
        "description": "Compact 75% mechanical gaming and productivity keyboard with hot-swappable tactile switches and double-shot PBT keycaps.",
        "price": 2199.0,
        "stock": 30,
        "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=600&auto=format&fit=crop&q=80"
    },
    {
        "category_slug": "electronics",
        "name": "StreamVision 4K Ultra HD Webcam",
        "slug": "streamvision-4k-webcam",
        "description": "Professional 4K streaming webcam with auto-framing, dual stereo noise-canceling microphones, and privacy shutter.",
        "price": 3499.0,
        "stock": 14,
        "image_url": "https://images.unsplash.com/photo-1588508065123-287b28e013da?w=600&auto=format&fit=crop&q=80"
    },

    # Fashion
    {
        "category_slug": "fashion",
        "name": "UrbanVenture Water-Resistant Backpack",
        "slug": "urbanventure-backpack",
        "description": "Ergonomic 22L commuter backpack with padded 16-inch laptop compartment, luggage strap, and water-repellent canvas.",
        "price": 1499.0,
        "stock": 40,
        "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=600&auto=format&fit=crop&q=80"
    },
    {
        "category_slug": "fashion",
        "name": "Classic Vintage Washed Denim Jacket",
        "slug": "classic-denim-jacket",
        "description": "Timeless 100% cotton denim jacket with reinforced stitching, dual chest pockets, and relaxed tailored fit.",
        "price": 2299.0,
        "stock": 22,
        "image_url": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=600&auto=format&fit=crop&q=80"
    },
    {
        "category_slug": "fashion",
        "name": "AeroStride Lightweight Runners",
        "slug": "aerostride-runners",
        "description": "Breathable knit running sneakers with responsive foam cushioning and high-traction rubber outsole.",
        "price": 1899.0,
        "stock": 35,
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80"
    },
    {
        "category_slug": "fashion",
        "name": "Solstice Polarized Sunglasses",
        "slug": "solstice-polarized-sunglasses",
        "description": "Classic wayfarer silhouette with UV400 polarized scratch-resistant lenses and lightweight acetate frame.",
        "price": 899.0,
        "stock": 50,
        "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=600&auto=format&fit=crop&q=80"
    },

    # Home & Kitchen
    {
        "category_slug": "home-kitchen",
        "name": "BaristaCraft Ceramic Pour-Over Dripper",
        "slug": "baristacraft-pour-over",
        "description": "Handcrafted ceramic coffee dripper engineered with spiral ribs for maximum thermal stability and balanced flavor extraction.",
        "price": 749.0,
        "stock": 28,
        "image_url": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&auto=format&fit=crop&q=80"
    },
    {
        "category_slug": "home-kitchen",
        "name": "HydroShield Insulated Steel Flask (750ml)",
        "slug": "hydroshield-insulated-flask",
        "description": "Double-wall vacuum-insulated stainless steel water bottle keeping beverages cold for 24 hours or hot for 12 hours.",
        "price": 699.0,
        "stock": 60,
        "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=600&auto=format&fit=crop&q=80"
    },
    {
        "category_slug": "home-kitchen",
        "name": "LuminaGlow Touch LED Desk Lamp",
        "slug": "luminaglow-led-desk-lamp",
        "description": "Eye-care adjustable desk lamp featuring 5 color temperature modes, stepless dimming, and integrated USB charging port.",
        "price": 1299.0,
        "stock": 20,
        "image_url": "https://images.unsplash.com/photo-1534353436294-0dbd4bdac845?w=600&auto=format&fit=crop&q=80"
    },

    # Books & Tech
    {
        "category_slug": "books-tech",
        "name": "The DevOps Handbook (Second Edition)",
        "slug": "devops-handbook",
        "description": "How to create world-class agility, reliability, and security in technology organizations by Gene Kim, Jez Humble, and Patrick Debois.",
        "price": 899.0,
        "stock": 45,
        "image_url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=600&auto=format&fit=crop&q=80"
    },
    {
        "category_slug": "books-tech",
        "name": "Clean Architecture: A Craftsman's Guide",
        "slug": "clean-architecture-guide",
        "description": "Universal rules of software architecture and practical structure design by Robert C. Martin.",
        "price": 799.0,
        "stock": 30,
        "image_url": "https://images.unsplash.com/photo-1532012164546-f432f2e3777a?w=600&auto=format&fit=crop&q=80"
    }
]
