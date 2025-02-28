# Xpath

## Example html

```html
<div data-automation-id="questionItem" class="css-55">
  <div id="QuestionId_rb1234b239bad4fe594702e43fe16f02f" class="-a-58">
    <div class="-P-59">
      <span class="-m-61" data-automation-id="questionTitle"
        ><span aria-level="2" role="heading"
          ><span
            data-automation-id="questionOrdinal"
            aria-hidden="false"
            class="-hr-63"
            >1.</span
          ><span class="text-format-content"
            ><span>Name |&nbsp;</span><span>姓名</span></span
          ><span
            aria-hidden="false"
            class="css-4"
            role="note"
            aria-label="Required to answer"
            data-automation-id="requiredStar"
          ></span></span
        ><span class="-ab-62"
          ><span
            class="css-1"
            id="QuestionInfo_rb1234b239bad4fe594702e43fe16f02f"
            aria-hidden="true"
            >Single line text.
          </span></span
        ><span class="-fm-64" role="log" aria-live="polite"></span
      ></span>
    </div>
    <div class="-kH-60"></div>
  </div>
  <div class="-bR-49">
    <div class="-a-66 lrp-text-container">
      <span class="-nb-73"
        ><input
          aria-label="Single line text"
          maxlength="4000"
          placeholder="Enter your answer"
          aria-labelledby="QuestionId_rb1234b239bad4fe594702e43fe16f02f QuestionInfo_rb1234b239bad4fe594702e43fe16f02f"
          class="-aq-72"
          spellcheck="true"
          data-automation-id="textInput"
      /></span>
    </div>
  </div>
</div>
```

The goal is to get the element based on `"Name |"` and get the input element right after it.

## Xpath

```python
"//div[@data-automation-id='questionItem']"
```

This selects all `<div>` elements with `data-automation-id="questionItem"`.

```python
"[.//span[contains(., '{0}')]]".replace("{0}", "Name |")
```

Filters the containers to only those that have a descendant `<span>` whose text contains `"Name |"`.  

---
>
> ```python
> ".//"
> ```
>
> Tells XPath to start the search for `<span>` elements from the current node (rather than from the root of the document). It means "all descendant `<span>` elements of the current node."  

> ```python
> ".,"
> ```
>
> Represents the string value (i.e., all the concatenated text) of the current `<span>` element being evaluated.  
> Which means it checks whether the text of that `<span>` includes the substring specified by {0}.
  
---

```python
"//input"
```

Finds any `<input>` element that is a descendant of the filtered container.
