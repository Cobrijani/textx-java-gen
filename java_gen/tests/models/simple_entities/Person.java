package com.github.cobrijani.textxspringdemo.domain;



// Autogenerated using domain lang.
public class Person {

  private String name;
  private int age;

  /**
   * Getter for name
   * @return value
   */
  public String getName(){
      return this.name;
  }

  /**
   * Setter for name
   * @param name new value
   */
  public void setName(String name){
    this.name = name;
  }

  /**
   * Getter for age
   * @return value
   */
  public int getAge(){
      return this.age;
  }

  /**
   * Setter for age
   * @param age new value
   */
  public void setAge(int age){
    this.age = age;
  }

  /**
   * Fluent interface setter for name
   * @param name new value to be set
   * @return this object
   */
  public Person name(String name){
    this.name = name;
    return this;
  }

  /**
   * Fluent interface setter for age
   * @param age new value to be set
   * @return this object
   */
  public Person age(int age){
    this.age = age;
    return this;
  }


  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    builder.append("Person").append("{");
    builder.append("Name=").append(name).append(";");
    builder.append("Age=").append(age).append(";");
    builder.append("}");
    return builder.toString();
  }
}