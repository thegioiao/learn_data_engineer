-- tạo schema / bảng mẫu cho POC
CREATE TABLE IF NOT EXISTS fact_daily_revenue (
  order_day date PRIMARY KEY,
  daily_revenue numeric
);

-- user dw_user, db ecom_dw được tạo bằng biến môi trường
