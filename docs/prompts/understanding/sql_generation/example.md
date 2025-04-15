# SQL Generation
Ask Nova to generate SQL queries from natural language descriptions.

### System Prompt Template
    You are an expert {user description} who can {description of task}.
    Follow these instructions:
    {enumerated instructions}

### User Prompt Template
    {DDL for database tables}
    
## Example
### Amazon Nova Pro System Prompt
    You are an expert SQL developer who can answer a natural language question using a SQL query.
    Follow these instructions:
    1. Analyze the DDL in the <schema> section and understand the relationships between tables.
    2. Read and understand the natural language question in <question>. 
    3. Think step by step about the tables and relationships involved, what the query needs to do, and put your thoughts in <thinking>
    4. Write the SQL query that answers the question, and put it in ```sql``` code blocks
    5. Add any helpful comments to explain key parts of the query under ### Notes ### 
    
### Amazon Nova Pro User Prompt
    <schema>
        CREATE TABLE customers (
            customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20),
            address VARCHAR(200),
            city VARCHAR(50),
            state VARCHAR(50),
            postal_code VARCHAR(20),
            country VARCHAR(50) DEFAULT 'USA',
            date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'suspended')),
            credit_limit DECIMAL(12, 2) DEFAULT 5000.00,
            loyalty_points INTEGER DEFAULT 0,
            last_login_date TIMESTAMP,
            marketing_opt_in BOOLEAN DEFAULT TRUE
        );

        CREATE TABLE orders (
            order_id SERIAL PRIMARY KEY,
            customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            amount DECIMAL(12, 2) NOT NULL,
            status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled', 'returned')),
            payment_method VARCHAR(50),
            shipping_address VARCHAR(200),
            shipping_city VARCHAR(50),
            shipping_state VARCHAR(50),
            shipping_postal_code VARCHAR(20),
            shipping_country VARCHAR(50) DEFAULT 'USA',
            tracking_number VARCHAR(100),
            notes TEXT,
            tax_amount DECIMAL(12, 2) DEFAULT 0.00,
            shipping_amount DECIMAL(12, 2) DEFAULT 0.00,
            discount_amount DECIMAL(12, 2) DEFAULT 0.00,
            coupon_code VARCHAR(50),
            sales_rep_id INTEGER,
            CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT
        );

        CREATE TABLE order_items (
            item_id SERIAL PRIMARY KEY,
            order_id INTEGER NOT NULL REFERENCES orders(order_id),
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 1,
            unit_price DECIMAL(12, 2) NOT NULL,
            discount_percent DECIMAL(5, 2) DEFAULT 0.00,
            subtotal DECIMAL(12, 2) GENERATED ALWAYS AS (quantity * unit_price * (1 - discount_percent/100)) STORED,
            CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
        );

        CREATE INDEX idx_orders_customer_id ON orders(customer_id);
        CREATE INDEX idx_orders_order_date ON orders(order_date);
        CREATE INDEX idx_orders_amount ON orders(amount);
        CREATE INDEX idx_order_items_order_id ON order_items(order_id);
        CREATE INDEX idx_order_items_product_id ON order_items(product_id);
    </schema>
    <question>Show me all customers who have made purchases over $1000 in the last 30 days, 
    along with their total spend and number of orders. Sort by total spend descending.</question>

### Amazon Nova Pro Sample Response
!!! success "Response"
    --8<-- "results/sql_generation_20250326_164152.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/sql_generation/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/sql_generation/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/sql_generation/example.json"
    ```