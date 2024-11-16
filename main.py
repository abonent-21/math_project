# main.py

import tkinter as tk
from tkinter import ttk, messagebox
import importlib
import os
import inspect
from Types import nat_0, dig, ceil, rat, pol


class ScrollableFrame(ttk.Frame):
    """
    Класс для создания прокручиваемого фрейма.
    """

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        canvas = tk.Canvas(self, borderwidth=0, background="#f0f0f0")
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas, padding=(10, 10, 10, 10))

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Настройка прокрутки колесиком мыши
        self.scrollable_frame.bind("<Enter>", lambda e: self._bind_to_mousewheel(canvas))
        self.scrollable_frame.bind("<Leave>", lambda e: self._unbind_from_mousewheel(canvas))

    def _on_mousewheel(self, event, canvas):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_to_mousewheel(self, canvas):
        canvas.bind_all("<MouseWheel>", lambda e: self._on_mousewheel(e, canvas))

    def _unbind_from_mousewheel(self, canvas):
        canvas.unbind_all("<MouseWheel>")


class MathApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Math Modules Interface")
        self.geometry("800x600")
        self.resizable(True, True)  # Разрешаем изменение размера окна
        self.current_frame = None
        self.show_main_menu()

    def show_frame(self, frame_class):
        """Переход на указанную фрейм-страницу."""
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_main_menu(self):
        self.show_frame(MainMenu)

    def show_category_menu(self, category):
        self.show_frame(lambda master: CategoryMenu(master, category))

    def show_function_menu(self, category, func_name):
        self.show_frame(lambda master: FunctionFrame(master, category, func_name))


class MainMenu(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = ttk.Label(self, text="Выберите категорию модулей", font=("Arial", 16))
        label.pack(pady=20)

        buttons = [
            ("Натуральные числа (N)", "natural_numbers"),
            ("Целые числа (Z)", "integers"),
            ("Рациональные числа (Q)", "rationals"),
            ("Многочлены (P)", "polynomials"),
        ]

        for (text, category) in buttons:
            btn = ttk.Button(self, text=text, width=30, command=lambda c=category: master.show_category_menu(c))
            btn.pack(pady=5)


class CategoryMenu(ttk.Frame):
    def __init__(self, master, category):
        super().__init__(master)
        self.category = category
        label = ttk.Label(self, text=f"=== {self.get_category_display()} ===", font=("Arial", 16))
        label.pack(pady=20)

        self.modules = self.get_modules()

        if not self.modules:
            ttk.Label(self, text="Нет доступных модулей для этой категории.", foreground="red").pack(pady=10)
        else:
            for key, func in sorted(self.modules.items(), key=lambda x: int(x[0])):
                btn = ttk.Button(self, text=f"{key}. {func}", width=40,
                                 command=lambda f=func: master.show_function_menu(self.category, f))
                btn.pack(pady=2)

        back_btn = ttk.Button(self, text="Назад", width=10, command=master.show_main_menu)
        back_btn.pack(pady=20)

    def get_category_display(self):
        mapping = {
            "natural_numbers": "Натуральные числа (N)",
            "integers": "Целые числа (Z)",
            "rationals": "Рациональные числа (Q)",
            "polynomials": "Многочлены (P)",
        }
        return mapping.get(self.category, "Категория")

    def get_modules(self):
        """Возвращает словарь {номер: имя функции} для заданной категории."""
        prefix_map = {
            "natural_numbers": ["COM_NN_D", "NZER_N_B", "ADD_1N_N", "ADD_NN_N", "SUB_NN_N",
                                "MUL_ND_N", "MUL_Nk_N", "MUL_NN_N", "SUB_NDN_N", "DIV_NN_Dk",
                                "DIV_NN_N", "MOD_NN_N", "GCF_NN_N", "LCM_NN_N"],
            "integers": ["ABS_Z_Z", "POZ_Z_D", "MUL_ZM_Z", "TRANS_N_Z", "TRANS_Z_N",
                         "ADD_ZZ_Z", "SUB_ZZ_Z", "MUL_ZZ_Z", "DIV_ZZ_Z", "MOD_ZZ_Z"],
            "rationals": ["RED_Q_Q", "INT_Q_B", "TRANS_Z_Q", "TRANS_Q_Z",
                          "ADD_QQ_Q", "SUB_QQ_Q", "MUL_QQ_Q", "DIV_QQ_Q"],
            "polynomials": ["ADD_PP_P", "SUB_PP_P", "MUL_PQ_P", "MUL_Pxk_P", "LED_P_Q",
                            "DEG_P_N", "FAC_P_Q", "MUL_PP_P", "DIV_PP_P", "MOD_PP_P",
                            "GCF_PP_P", "DER_P_P", "NMR_P_P"]
        }

        functions = prefix_map.get(self.category, [])
        modules = {}
        for func in functions:
            if os.path.exists(f"{func}.py"):
                # Извлекаем номер функции из имени, например, COM_NN_D -> 1, 2 и т.д.
                # Здесь предполагается, что после первого разделителя идет номер
                parts = func.split('_')
                number = ''
                for part in parts:
                    if part.isdigit():
                        number = part
                        break
                if not number:
                    # Если номер не найден, присвоим уникальный ключ
                    number = str(len(modules) + 1)
                modules[number] = func
        return modules


class FunctionFrame(ttk.Frame):
    def __init__(self, master, category, func_name):
        super().__init__(master)
        self.category = category
        self.func_name = func_name
        self.func = self.get_function(func_name)
        if self.func is None:
            messagebox.showerror("Ошибка", f"Не удалось загрузить функцию {func_name}")
            master.show_category_menu(category)
            return

        label = ttk.Label(self, text=f"=== {func_name} ===", font=("Arial", 16))
        label.pack(pady=10)

        # Используем ScrollableFrame для размещения полей ввода
        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        self.inputs_frame = self.scrollable_frame.scrollable_frame

        self.input_vars = {}
        self.polynomials = {}  # Словарь для хранения многочленов по параметрам
        self.create_input_fields()

        execute_btn = ttk.Button(self, text="Выполнить", command=self.execute_function)
        execute_btn.pack(pady=10)

        back_btn = ttk.Button(self, text="Назад", command=lambda: master.show_category_menu(category))
        back_btn.pack()

        # Создание фрейма для результата и кнопки копирования
        result_frame = ttk.Frame(self)
        result_frame.pack(pady=10, padx=10, fill=tk.X)

        self.result_var = tk.StringVar()
        self.result_entry = ttk.Entry(result_frame, textvariable=self.result_var, font=("Arial", 14), state='readonly')
        self.result_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        copy_btn = ttk.Button(result_frame, text="Копировать", command=self.copy_result)
        copy_btn.pack(side=tk.RIGHT, padx=5)

    def copy_result(self):
        """Копирует текст результата в буфер обмена."""
        result_text = self.result_var.get()
        if result_text:
            self.clipboard_clear()
            self.clipboard_append(result_text)
            self.update()  # Обновление для гарантии, что данные попадут в буфер обмена
            messagebox.showinfo("Успех", "Результат скопирован в буфер обмена.")
        else:
            messagebox.showwarning("Внимание", "Нет результата для копирования.")

    def get_function(self, func_name):
        try:
            module = importlib.import_module(func_name)
            func = getattr(module, func_name)
            return func
        except Exception as e:
            messagebox.showerror("Ошибка импорта", f"Не удалось импортировать {func_name}: {e}")
            return None

    def create_input_fields(self):
        """Создает поля ввода на основе параметров функции с использованием inspect."""
        params = inspect.signature(self.func).parameters
        row = 0
        for param_name, param in params.items():
            # Определяем тип параметра на основе аннотаций
            annotation = param.annotation
            annotation_name = annotation.__name__ if hasattr(annotation, '__name__') else str(annotation)

            # Создаем метку и поле ввода
            label_text = f"{param_name} ({annotation_name}):"
            ttk.Label(self.inputs_frame, text=label_text).grid(row=row, column=0, sticky=tk.W, pady=2, padx=5)

            if annotation_name == 'pol':
                # Для многочленов используем специальный ввод с передачей имени параметра
                btn = ttk.Button(self.inputs_frame, text=f"Ввести многочлен {param_name}",
                                 command=lambda p=param_name: self.open_polynomial_input(p))
                btn.grid(row=row, column=1, sticky=tk.W, pady=2, padx=5)
                self.input_vars[param_name] = tk.StringVar()
                # Инициализируем пустой многочлен для этого параметра
                self.polynomials[param_name] = None
            else:
                self.input_vars[param_name] = tk.StringVar()
                entry = ttk.Entry(self.inputs_frame, textvariable=self.input_vars[param_name], width=50)
                entry.grid(row=row, column=1, pady=2, padx=5)
            row += 1

    def open_polynomial_input(self, param_name):
        """Открывает отдельное окно для ввода многочлена."""
        self.poly_window = tk.Toplevel(self)
        self.poly_window.title(f"Ввод Многочлена для {param_name}")
        self.poly_window.geometry("500x600")
        self.poly_window.grab_set()

        # Создаём ScrollableFrame внутри Toplevel окна
        scrollable = ScrollableFrame(self.poly_window)
        scrollable.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        frame = scrollable.scrollable_frame

        ttk.Label(frame, text="Введите степень многочлена:", font=("Arial", 12)).pack(pady=10)
        self.degree_var = tk.IntVar(value=0)
        self.degree_spinbox = ttk.Spinbox(frame, from_=0, to=100, textvariable=self.degree_var, width=5,
                                          command=self.create_poly_coeff_fields)
        self.degree_spinbox.pack()

        self.coeff_frame = ttk.Frame(frame)
        self.coeff_frame.pack(pady=10)

        self.coeff_vars = {}

        submit_btn = ttk.Button(frame, text="Сохранить", command=lambda p=param_name: self.save_polynomial(p))
        submit_btn.pack(pady=10)

        self.create_poly_coeff_fields()  # Создать поля для степени 0 по умолчанию

    def create_poly_coeff_fields(self):
        """Создает поля ввода для коэффициентов многочлена на основе степени."""
        # Очищаем предыдущие поля
        for widget in self.coeff_frame.winfo_children():
            widget.destroy()
        self.coeff_vars.clear()

        try:
            degree = int(self.degree_var.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Степень должна быть целым числом.")
            return

        for i in range(degree + 1):
            frame = ttk.Frame(self.coeff_frame)
            frame.pack(anchor='w', pady=2, padx=5)
            ttk.Label(frame, text=f"Коэффициент при x^{i} (формат: числитель/знаменатель):").pack(side=tk.LEFT)
            var = tk.StringVar()
            ttk.Entry(frame, textvariable=var, width=30).pack(side=tk.LEFT, padx=5)
            self.coeff_vars[i] = var

    def save_polynomial(self, param_name):
        """Сохраняет введённые коэффициенты и закрывает окно ввода."""
        degree = self.degree_var.get()
        coefficients = []
        for i in range(degree + 1):
            coef_str = self.coeff_vars[i].get().strip()
            if not coef_str:
                # Приравниваем к 0: 0/1
                coef_str = "0/1"
            try:
                num_str, den_str = coef_str.split('/')
                num = self.parse_ceil(num_str.strip())
                den = self.parse_nat_0(den_str.strip())
                if num is None or den is None:
                    return
                coefficients.append(rat(num, den))
            except ValueError:
                messagebox.showerror("Ошибка",
                                     f"Некорректный формат коэффициента при x^{i}. Ожидается числитель/знаменатель.")
                return
        self.polynomials[param_name] = pol(coefficients, degree)

        # Отладочный вывод
        print(f"Сохранённый многочлен для {param_name}: {self.polynomials[param_name]}")

        # Обновляем соответствующее поле ввода в основном окне
        self.input_vars[param_name].set(str(self.polynomials[param_name]))
        self.poly_window.destroy()

    def execute_function(self):
        """Собирает вводимые данные, вызывает функцию и отображает результат."""
        try:
            params = inspect.signature(self.func).parameters
            args = []
            for param_name, param in params.items():
                input_str = self.input_vars.get(param_name).get().strip()
                if 'nat_0' in str(param.annotation):
                    obj = self.parse_nat_0(input_str)
                elif 'dig' in str(param.annotation):
                    obj = self.parse_dig(input_str)
                elif 'ceil' in str(param.annotation):
                    obj = self.parse_ceil(input_str)
                elif 'rat' in str(param.annotation):
                    obj = self.parse_rat(input_str)
                elif 'pol' in str(param.annotation):
                    if self.polynomials.get(param_name):
                        obj = self.polynomials[param_name]
                    else:
                        # Если поле пустое и тип pol, приравниваем к нулевому многочлену
                        obj = pol([rat(ceil([0], 1, 0), nat_0([1], 1))], 0)
                else:
                    # Для простых типов, например, int
                    if not input_str:
                        # Если поле пустое, приравниваем к нулю
                        input_str = "0"
                    try:
                        obj = int(input_str)
                    except ValueError:
                        messagebox.showerror("Ошибка",
                                             f"Некорректный ввод для параметра {param_name}. Ожидается {param.annotation.__name__}.")
                        return
                if obj is None:
                    # Если парсинг не удался, прерываем выполнение
                    return
                args.append(obj)

            # Отладочный вывод аргументов
            print(f"Вызов функции {self.func_name} с аргументами: {args}")

            result = self.func(*args)

            # Отладочный вывод результата
            print(f"Результат функции {self.func_name}: {result}")

            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении функции: {e}")

    def parse_nat_0(self, input_str):
        """Парсит строку в nat_0. Пустая строка приравнивается к 0."""
        if not input_str:
            # Приравниваем к 0: nat_0([0], 1)
            return nat_0([0], 1)
        try:
            digits = [int(d) for d in input_str.strip()]
            if not digits:
                messagebox.showerror("Ошибка", "Натуральное число не может быть пустым.")
                return None
            if not all(0 <= d <= 9 for d in digits):
                messagebox.showerror("Ошибка", "Все символы должны быть цифрами от 0 до 9.")
                return None
            return nat_0(digits, len(digits))
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод для натурального числа.")
            return None

    def parse_dig(self, input_str):
        """Парсит строку в dig. Пустая строка приравнивается к 0."""
        if not input_str:
            # Приравниваем к 0: dig(0)
            return dig(0)
        try:
            number = int(input_str)
            if not (0 <= number <= 9):
                messagebox.showerror("Ошибка", "Цифра должна быть от 0 до 9.")
                return None
            return dig(number)
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод для цифры.")
            return None

    def parse_ceil(self, input_str):
        """Парсит строку в ceil. Пустая строка приравнивается к 0."""
        if not input_str:
            # Приравниваем к 0: ceil([0], 1, 0)
            return ceil([0], 1, 0)
        try:
            sign = 0
            if input_str.startswith('-'):
                sign = 1
                digits_str = input_str[1:]
            else:
                digits_str = input_str
            digits = [int(d) for d in digits_str.strip()]
            if not digits:
                messagebox.showerror("Ошибка", "Число не может быть пустым.")
                return None
            if not all(0 <= d <= 9 for d in digits):
                messagebox.showerror("Ошибка", "Все символы должны быть цифрами от 0 до 9.")
                return None
            return ceil(digits, len(digits), sign)
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод для целого числа.")
            return None

    def parse_rat(self, input_str):
        """Парсит строку в rat. Пустая строка приравнивается к 0/1."""
        if not input_str:
            # Приравниваем к 0/1: rat(ceil([0],1,0), nat_0([1],1))
            return rat(ceil([0], 1, 0), nat_0([1], 1))
        try:
            num_str, den_str = input_str.split('/')
            num = self.parse_ceil(num_str.strip())
            den = self.parse_nat_0(den_str.strip())
            if num is None or den is None:
                return None
            if den.array == [0] * den.n:
                messagebox.showerror("Ошибка", "Знаменатель не может быть равен нулю.")
                return None
            return rat(num, den)
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод для рационального числа. Формат: числитель/знаменатель.")
            return None

    def display_result(self, result):
        """Отображает результат."""
        self.result_var.set(f"Результат: {result}")


if __name__ == "__main__":
    app = MathApp()
    app.mainloop()
