# Tasknote CLI — Progress Summary & AI Handoff Guide

## Purpose of this file
This file is a handoff summary for any AI language model helping with this project.

It should help the model:
- understand the current state of the project
- understand the user's skill level and preferences
- continue the project without restarting or overcomplicating things
- follow the user's instruction style
- always check whether the GitHub repo has been connected to the local machine before giving repo-related steps

---

## Project overview
The user is building a beginner-friendly Python CLI task tracker inspired by the roadmap.sh task tracker project.

The project is currently being built **without classes**.

The user is intentionally using:
- functions
- lists
- dictionaries
- shlex
- simple terminal input loop

The current goal is to finish the CLI version first before making it more advanced.

---

## Important user preferences
Any AI helping with this project should follow these rules:

1. **Do not overfocus on unrelated parts of the code**
   - If the user asks about one function, only help with that function unless another issue directly blocks it.

2. **Explain in beginner-friendly plain English**
   - The user is learning by building.
   - Keep explanations practical and direct.

3. **Do not force classes or OOP**
   - The current project is intentionally being built without classes.
   - Continue using functions + list of dictionaries unless the user explicitly asks to refactor.

4. **Build one feature at a time**
   - Do not jump ahead and rewrite the whole program.
   - Keep the development order small and practical.

5. **Always check repo connection first when repo/git setup is relevant**
   - Before giving repo-related next steps, ask:
     - "Have you connected the repo to your local machine yet?"
   - If the answer is no, guide the user through connecting the repo locally before continuing.
   - If the answer is yes, continue with the requested development help.

6. **Respect the user's style**
   - The user often wants:
     - only the exact part fixed
     - no unnecessary cleanup
     - no full rewrite unless requested

---

## Mandatory repo check instruction for future AI help
If the user asks anything involving:
- GitHub repo
- pushing code
- pulling code
- connecting project files
- cloning
- local folder setup
- branch setup
- committing or syncing work

Then the AI should first ask:

**"Have you connected the repo to your local machine yet?"**

If the answer is **no**, guide them through:
1. checking current folder
2. checking whether Git is initialized
3. checking remote connection
4. cloning or linking the repo properly
5. confirming that local and remote are connected

Only after that should the AI continue with repo-related instructions.

---

## Current project structure and logic
The app currently uses:
- `tasks = []` as in-memory storage
- each task is a dictionary
- a main input loop using `input(">:")`
- `shlex.split()` to parse commands
- command routing using `filter_info()`

Each task currently looks like:

```python
{
    "id": 1,
    "description": "Buy groceries",
    "status": "todo"
}
```

---

## Current implemented features
These features are already working or mostly working:

### 1. Add task
Command pattern:
```text
add "Buy groceries"
```

Current behavior:
- creates a new dictionary task
- assigns:
  - id
  - description
  - status = "todo"
- appends task to `tasks`
- prints success message

Current function:
- `adding_info(follow_up=None)`

---

### 2. List tasks
Command pattern:
```text
list
```

Current behavior:
- if no tasks, prints "No task yet"
- otherwise loops through `tasks`
- formats each task for display

Current functions:
- `listing_info()`
- `formating_data(info_filter)`

Current formatting style:
```text
ID: 1 | Description:Buy groceries | Status: todo
```

---

### 3. Delete task
Command pattern:
```text
delete 2
```

Current behavior:
- deletes a task by entered id position
- renumbers remaining tasks so ids become sequential again
- prints deleted task

Current function:
- `delete_fuc(index=None)`

Important note:
- This app currently **renumbers ids after deletion**
- That is acceptable for this beginner version
- Future AI should not fight this unless the user wants permanent ids

---

### 4. Update task description
Command pattern:
```text
update 2 "Buy groceries and cook dinner"
```

Current behavior:
- checks for missing id/description
- converts id to int
- finds matching task
- updates the `description`
- prints success message
- prints "Task not found" if missing

Current function:
- `update_fuc(id=None, new_text=None)`

---

### 5. Help command
Command pattern:
```text
/help
```

Current behavior:
- prints available commands list

---

### 6. Quit command
Command pattern:
```text
quit
```

Current behavior:
- returns `False` from `slicing_info()`
- main loop stops

---

## Current code flow
The current high-level flow is:

```text
user input
   ->
slicing_info()
   ->
shlex.split()
   ->
filter_info()
   ->
route to function
   ->
modify tasks or display tasks
```

---

## Current code style
The code is still intentionally beginner-style and should stay understandable.

The AI should preserve this style:
- simple functions
- no advanced abstractions unless asked
- no class refactor
- no unnecessary optimization
- no major structural rewrite unless requested

---

## Known project choices
These are current design decisions and should be respected unless the user asks otherwise:

1. **No classes**
2. **In-memory task storage first**
3. **IDs are renumbered after deletion**
4. **Formatting is separate from storage**
5. **Feature-by-feature development**
6. **CLI-first design**
7. **shlex is used for parsing commands with quoted text**

---

## Known issue / caution
### Lowercasing entire input
Current code lowercases the full input line in `slicing_info()`:

```python
slicer = slicer.strip().lower()
```

That means task descriptions also become lowercase.

Example:
```text
add "Buy Groceries for Mom"
```

becomes:
```text
buy groceries for mom
```

This is a known behavior. It is not urgent unless the user wants to preserve original capitalization.

Future AI can suggest improving this later by lowercasing only the command part, but should not derail the current task unless the user asks.

---

## Current development stage
The project is currently at this stage:

### Done
- input loop
- command parsing
- help
- quit
- add
- list
- delete
- update
- formatting for list output

### Next recommended goals
The next best features to build are:

1. `mark-in-progress`
2. `mark-done`
3. `list done`
4. `list todo`
5. `list in-progress`
6. save/load tasks to JSON
7. polish input validation
8. optional README / repo cleanup later

---

## Recommended build order from this point
Any AI continuing the project should use this order:

```text
1. mark-in-progress
2. mark-done
3. list by status
4. save tasks to JSON
5. load tasks from JSON on startup
6. improve validation and messages
```

---

## Suggested next function design
To avoid repeated code, future AI may recommend a helper like:

```text
change_status(task_id, new_status)
```

This can be used for:
- `mark-in-progress`
- `mark-done`

But keep it beginner-friendly.

---

## Current command list
The help output currently uses these commands:

```text
add "Buy groceries"
update 1 "Buy groceries and cook dinner"
delete 1
mark-in-progress 1
mark-done 1
list
list done
list todo
list in-progress
```

---

## Important instruction on code help style
If the user pastes code and asks a question, future AI should:

- answer the exact issue first
- explain why the issue happens
- give the smallest practical fix
- avoid rewriting the full project unless the user asks for a full rewrite
- preserve the user's variable and function naming unless a rename is necessary to fix a bug

---

## Important instruction on teaching style
The user is learning through repetition and practical building.

That means future AI should:
- break problems into tiny steps
- explain the "why"
- show what the next milestone is
- avoid making the project feel bigger than it is

Helpful framing:
- "delete is like update's cousin"
- "formatting is for display, not storage"
- "build one command at a time"

This teaching style is working well and should be maintained.

---

## Example status summary for future AI
If asked "where are we now?", a good short answer would be:

```text
You have:
- add
- list
- delete
- update
- help
- quit

Next best step:
- mark-in-progress
- mark-done
- list by status
- JSON save/load
```

---

## Final instruction to future AI
Before helping with any repo / GitHub / sync issue, always ask:

**Have you connected the repo to your local machine yet?**

If not, help the user connect it first.

Before helping with code, continue from the current function-based CLI structure and do not push classes unless the user explicitly requests that change.
