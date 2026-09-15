local toolbar = plugin:CreateToolbar("Rooms Progress")

local button = toolbar:CreateButton(
	"Scan Rooms",
	"Scan the current place for completed rooms",
	""
)

local HttpService = game:GetService("HttpService")

button.Click:Connect(function()
	print("===== ROOM SCANNER =====")

	local rooms = {}

	for _, obj in ipairs(workspace:GetDescendants()) do
		if obj:IsA("TextLabel") or obj:IsA("TextButton") or obj:IsA("TextBox") then
			local number = string.match(obj.Text, "^B%-(%d%d%d%d)$")

			if number then
				rooms[tonumber(number)] = true
			end
		end
	end

	local highestRoom = 0
	local roomCount = 0

	for number in pairs(rooms) do
		roomCount += 1

		if number > highestRoom then
			highestRoom = number
		end
	end

	local completedrooms = highestRoom - 1
	local percent = (completedrooms / 1000) * 100

	print("--------------------")
	print("UNIQUE ROOMS:", roomCount)
	print("HIGHEST ROOM:", highestRoom)
	print("PROGRESS:", completedrooms .. " / 1000")
	print("PERCENT:", percent .. "%")

	-- Send progress to Python
	local data = {
		rooms = completedrooms,
		total = 1000,
		percent = percent
	}

	local json = HttpService:JSONEncode(data)

	local success, response = pcall(function()
		return HttpService:PostAsync(
			"http://127.0.0.1:8000/progress",
			json,
			Enum.HttpContentType.ApplicationJson
		)
	end)

	if success then
		print("PYTHON RESPONSE:", response)
	else
		warn("FAILED TO SEND TO PYTHON:", response)
	end

	print("===== ROOM SCANNER FINISHED =====")
end)