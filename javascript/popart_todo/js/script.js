window.addEventListener("load", () => {
  //todos = localStorage.getItem("todos") || [];

  const form = document.querySelector("#task-form");
  const input = document.querySelector("#task-input");
  const list_el = document.querySelector("#tasks");

  //list_el.value = todos;

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const task = input.value;

    if (!task) {
      alert("Please add a task!");
    } else {
      // Consts

      const task_el = document.createElement("div");
      task_el.classList.add("task");

      const task_content_el = document.createElement("div");
      task_content_el.classList.add("content");

      const task_input_el = document.createElement("input");
      task_input_el.classList.add("text");
      task_input_el.type = "text";
      task_input_el.value = task;
      task_input_el.setAttribute("readonly", "readonly");

      const task_actions_el = document.createElement("div");
      task_actions_el.classList.add("actions");

      const task_edit_el = document.createElement("button");
      task_edit_el.classList.add("edit");
      task_edit_el.innerHTML = "Edit";

      const task_delete_el = document.createElement("button");
      task_delete_el.classList.add("delete");
      task_delete_el.innerHTML = "Delete";

      // Appends

      task_actions_el.appendChild(task_edit_el);
      task_actions_el.appendChild(task_delete_el);

      task_content_el.appendChild(task_input_el);

      task_el.appendChild(task_content_el);
      task_el.appendChild(task_actions_el);
      list_el.appendChild(task_el);

      input.value = "";

      //todos.push(list_el);
      //localStorage.setItem("todos", todos);

      // Actions

      task_edit_el.addEventListener("click", () => {
        if (task_edit_el.innerText.toLowerCase() == "edit") {
          task_input_el.removeAttribute("readonly");
          task_input_el.focus();
          task_edit_el.innerText = "Save";
        } else {
          task_input_el.setAttribute("readonly", "readonly");
          task_edit_el.innerText = "Edit";
        }
      });

      task_delete_el.addEventListener("click", () => {
        if (confirm("Are you sure you want to delete this?")) {
          list_el.removeChild(task_el);
        }
      });
    }
  });
});

// Hipótese: Para adicionar local storage eu preciso guardar a variável list_el e adiciona-la ao html quando a página for carregada
