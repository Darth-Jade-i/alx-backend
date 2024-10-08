import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Fetch product by ID
function getItemById(id) {
    return listProducts.find(product => product.id === id);
}

// Route for listing all products
app.get('/list_products', (req, res) => {
    res.json(listProducts.map(product => ({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock
    })));
});

// Route for individual product
app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);
    
    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const reservedStock = await getAsync(`item.${itemId}`);
    const currentQuantity = product.stock - (reservedStock ? reservedStock : 0);

    res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity
    });
});

// Route for reserving product
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);

    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const reservedStock = await getAsync(`item.${itemId}`);
    const currentStock = product.stock - (reservedStock ? reservedStock : 0);

    if (currentStock <= 0) {
        return res.json({ status: 'Not enough stock available', itemId });
    }

    client.incr(`item.${itemId}`);
    res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
