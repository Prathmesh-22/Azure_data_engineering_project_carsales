# Databricks notebook source
# MAGIC %md
# MAGIC Create Catalog
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG cars_catalog; --catalog is database

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create Schema

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA cars_catalog.silver;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA cars_catalog.gold;