#include "lists.h"
/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the first node in the list
 *
 * Return: Pointer to the first node in the new list
 */
void reverse_list(node **head)
{
	node *prev = NULL;
	node *current = *head;
	node *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the linked list
 *
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(node **head)
{
	node *slow = *head;
	node *fast = *head;
	node *temp = *head;
	node *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_list(&dup);

	while (dup && temp)
	{
		if (temp->data == dup->data)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);
	return (0);
}
