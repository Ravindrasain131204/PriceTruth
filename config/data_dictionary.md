# PRICE TRUTH - Data Dictionary

## Purpose
This document defines the structure of product price
observations collected for the Price Truth project.

## Dataset Fields

| Column | Description | Data Type |
|---|---|---|
| observation_id | Unique observation ID | String |
| product_id | Unique product ID | String |
| product_name | Product name | String |
| brand | Product brand | String |
| category | Product category | String |
| platform | Shopping platform | String |
| product_url | Original product URL | String |
| seller_name | Seller name | String |
| price_inr | Observed selling price | Float |
| mrp_inr | Listed MRP | Float |
| currency | Currency code | String |
| availability | Product stock status | String |
| observed_at | Date and time of observation | Datetime |
| source_type | Data collection method | String |

## Data Quality Rules

1. Product prices must be positive.
2. Currency must be recorded correctly.
3. Observation timestamps must be preserved.
4. Missing values must not be replaced with fake data.
5. Product URLs must be stored for verification.
6. Historical prices must come from actual observations.