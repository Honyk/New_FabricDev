CREATE TABLE [dbo].[Sales_Dup] (

	[SalesOrderNumber] varchar(8000) NULL, 
	[SalesOrderLineNumber] bigint NULL, 
	[OrderDate] date NULL, 
	[CustomerName] varchar(8000) NULL, 
	[EmailAddress] varchar(8000) NULL, 
	[Item] varchar(8000) NULL, 
	[Quantity] bigint NULL, 
	[UnitPrice] float NULL, 
	[TaxAmount] float NULL
);

