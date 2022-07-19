package com.github.cobrijani.textxspringdemo.domain;



// Autogenerated using domain lang.
public class ProductItem {

  private String itemName;

  /**
   * Getter for itemName
   * @return value
   */
  public String getItemname(){
      return this.itemName;
  }

  /**
   * Setter for itemName
   * @param itemName new value
   */
  public void setItemname(String itemName){
    this.itemName = itemName;
  }

  /**
   * Fluent interface setter for itemName
   * @param itemName new value to be set
   * @return this object
   */
  public ProductItem itemName(String itemName){
    this.itemName = itemName;
    return this;
  }


  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    builder.append("ProductItem").append("{");
    builder.append("Itemname=").append(itemName).append(";");
    builder.append("}");
    return builder.toString();
  }
}