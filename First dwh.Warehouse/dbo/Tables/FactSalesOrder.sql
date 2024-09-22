CREATE TABLE [dbo].[FactSalesOrder] (

	[SalesOrderKey] int NOT NULL, 
	[SalesOrderDateKey] int NOT NULL, 
	[ProductKey] int NOT NULL, 
	[CustomerKey] int NOT NULL, 
	[Quantity] int NULL, 
	[SalesTotal] decimal(18,0) NULL
);


GO
ALTER TABLE [dbo].[FactSalesOrder] ADD CONSTRAINT FK_0bfae592_13ff_40b9_98e3_91e6abdd44df FOREIGN KEY ([ProductKey]) REFERENCES dbo.DimProduct([ProductKey]);
GO
ALTER TABLE [dbo].[FactSalesOrder] ADD CONSTRAINT FK_275c3183_f36c_41aa_98d4_eaadd50f7d95 FOREIGN KEY ([CustomerKey]) REFERENCES dbo.DimCustomer([CustomerKey]);
GO
ALTER TABLE [dbo].[FactSalesOrder] ADD CONSTRAINT FK_f4316cc8_752f_4b42_896b_3c2f36b98c7f FOREIGN KEY ([SalesOrderDateKey]) REFERENCES dbo.DimDate([DateKey]);